# -*- coding: utf-8 -*-
# @Author: hanjiyun
# @Date:   2016-11-12 20:49:20
# @Last Modified by:   hanjiyun
# @Last Modified time: 2016-12-25 15:34:59
# Thanks http://www.patrickcai.com/

from flask import Flask, render_template, request, jsonify, abort, make_response
from flaskrun import flaskrun

import user
import scrobble
import database
from datetime import datetime, timedelta
from scheduler import Scheduler
from config import tasks
from itertools import izip

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/first')
def first():
    return render_template('first.html')

@app.route('/second')
def second():
    user_ID = request.args.get('username', '')
    (url, network) = user.get_url(user_ID)
    return render_template('second.html', url=url)

@app.route('/third')
def third():
    token = request.args.get('token')
    user_ID = request.args.get('username')
    is_preview = request.args.get('is_preview')

    if is_preview == '1':
        return render_template('third.html')
    else:
        try:
            session = scrobble.get_session(token)
        except Exception as e:
            return render_template('error.html', error='网页已过期'), 401
        record_time = datetime.now() - timedelta(minutes=20)
        record_time = record_time.strftime('%Y-%m-%d %H:%M:%S')
        database.insert_user(user_ID, session, record_time)
        return render_template('third.html')


@app.route('/auto_comment')
def auto_comment():
    return jsonify({
            'err': 0
        })

# @app.route('/sync')
# def sync():
#     try:
#         sync_handler()
#         return 'sync success'
#     except Exception as e:
#         print e
#         return render_template('error.html', error=e), 500

# @app.route('/favorite')
# def favorite():
#     try:
#         favorite_handler()
#         return 'favorite success'
#     except Exception as e:
#         print e
#         return render_template('error.html', error=e), 500


def favorite_handler():
    number_of_task = tasks
    all_users = database.get_all_users()
    all_users = sorted(all_users, key=lambda x:x[0])
    slice_number = len(all_users) / 5
    if number_of_task != 4:
        users = all_users[number_of_task*slice_number:
                          (number_of_task+1)*slice_number]
    elif number_of_task == 4:
        users = all_users[number_of_task * slice_number:
                          len(all_users)]
    for user in users:
        loved_songs = scrobble.xiami_loved(user)
        if loved_songs:
            try:
                print '[favorite] -  %s - %s - %s' % (user, loved_songs[0].title, loved_songs[0].artist)
                print '='*20
                scrobble.lastfm_loved(loved_songs, user)
                print 'Loved!'
            except Exception as e:
                print 'favorite error!'
                raise e
            # print '[favorite] -  %s - %s - %s' % (user, loved_songs[0].title, loved_songs[0].artist)
            # scrobble.lastfm_loved(loved_songs, user)
            # print 'Loved!'


def sync_handler():
    #read the user list from database
    users = database.get_user()

    for user in users:
        #read playing songs from the xiami
        titles, artists, track_times, record_time = scrobble.xiami(user)
        if titles:
            try:
                # print '[sync] - user: %s : titles: %s, artists: %s ' % (user, titles, artists)
                print 'sync_handler = ' * 5
                for title, artist in izip(titles, artists):
                    print '%s: %s - %s' % (user, artist, title)
                print '='*20
                scrobble.lastfm(titles, artists, track_times, user)
                #modify the user information
                database.modify_user(user[0], record_time)
                print 'Synced!'
            except Exception as e:
                print 'sync error!'
                raise e
            # print '[sync] - user: %s : titles: %s, artists: %s ' % (user, titles, artists)
            # scrobble.lastfm(titles, artists, track_times, user)
            # #modify the user information
            # database.modify_user(user[0], record_time)
            # print 'Synced!'


@app.route('/verify', methods=['POST'])
def verify():
    user_ID = request.form['username']
    should_continued = user.verify_user(user_ID)
    return jsonify({'continued': should_continued})


@app.errorhandler(401)
def not_found(error):
    resp = make_response(render_template('error.html'), 401)
    return resp

@app.errorhandler(500)
def not_found(error):
    resp = make_response(render_template('error.html'), 500)
    return resp


if __name__ == '__main__':
    scheduler_sync = Scheduler(10*60, sync_handler) #10 分钟更新一次
    #scheduler_love = Scheduler(60*60*24, favorite_handler) #24 小时更新一次
    scheduler_sync.start()
    # scheduler_love.start()
    # app.debug = False
    # app.run()
    flaskrun(app)
    scheduler_sync.stop()
    #scheduler_love.stop()
