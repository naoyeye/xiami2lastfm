# -*- coding: utf-8 -*-
# @Author: hanjiyun
# @Date:   2016-11-12 20:54:26
# @Last Modified by:   hanjiyun
# @Last Modified time: 2016-11-13 09:36:27

# Thanks http://www.patrickcai.com/

#! /usr/bin/env python
# -- encoding:utf - 8 --

import sys
import requests
import re
import urllib2
import pylast
import database
import logging
from config import API_KEY, API_SECRET

reload(sys)
sys.setdefaultencoding('utf-8')

def verify_user(user_ID):
    should_continue = database.is_user_exist(user_ID)
    return should_continue

def get_url(user_ID):
    network = pylast.LastFMNetwork(api_key = API_KEY, api_secret = API_SECRET)
    sg = pylast.SessionKeyGenerator(network)
    
    callback_url= 'http://xiami2lastfm.han.im/third?username=%s'%(user_ID)
    url = sg.get_web_auth_url(callback_url)
    return url, network


if __name__ == '__main__':
    verify_user(180848)