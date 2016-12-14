# -*- coding: utf-8 -*-
# @Author: hanjiyun
# @Date:   2016-12-14 13:22:26
# @Last Modified by:   hanjiyun
# @Last Modified time: 2016-12-14 14:38:58

from bs4 import BeautifulSoup

def xiami_comment(user):
  pass


def test():
  pass
  # var trlength =  $('.track_list tr').size();
  # var marked = 0;

  # $('.track_list tr').each(function(index, e){
  #   var oid = $(e).attr('id').replace('lib_song_', '');

  #   (function(ind) {
  #     setTimeout(function(){
  #       console.log('oid = ', oid);
  #       addCommet(oid)
  #     }, 1000 + (1200 * ind));
  #   })(index);
  # })

  # function addCommet(oid) {
  #   $.ajax({
  #     url: 'http://www.xiami.com/commentlist/add?type=4&oid=' + oid + '&content=%EF%BC%8F%EF%BC%8F%EF%BC%8F%EF%BC%8F%EF%BC%8F%EF%BC%8F%E5%A5%BD%E5%90%AC%EF%BC%81%EF%BC%8F%EF%BC%8F%EF%BC%8F%EF%BC%8F%EF%BC%8F%EF%BC%8F%EF%BC%8F%E2%80%A8%0A%EF%BC%8F%EF%BC%8F%E5%B0%8F%E7%8C%AB%E5%B0%8F%E7%8B%97%E5%B0%8F%E9%B8%A1%E5%B0%8F%E9%B8%AD%E5%B0%8F%E7%89%9B%E5%B0%8F%E7%8C%AA%EF%BC%8F%EF%BC%8F%0A%EF%BC%8F%EF%BC%8F%EF%BC%8F%E2%95%AD%E2%95%AE%EF%BC%8F%E2%95%AD%E2%95%AE%EF%BC%8F%EF%BC%8F%EF%BC%8F%EF%BC%8F%EF%BC%8F%EF%BC%8F%EF%BC%8F%EF%BC%8F+%0A%EF%BC%8F%EF%BC%8F%EF%BC%8F%E2%94%83%E2%94%97%E2%94%81%E2%94%9B%E2%94%83%EF%BC%8F%EF%BC%8F%EF%BC%8F%EF%BC%8F%EF%BC%8F%EF%BC%8F%EF%BC%8F%EF%BC%8F+%0A%EF%BC%8F%EF%BC%8F%EF%BC%8F%E2%94%83%E2%96%8B%E2%94%88%E2%96%8B%E2%94%A3%E2%94%81%E2%94%81%E2%94%81%E2%94%81%E2%95%AE%E2%95%AD%E2%95%AE%EF%BC%8F+%0A%EF%BC%8F%EF%BC%8F%E2%95%AD%E2%94%BB%E2%94%81%E2%95%AE%E2%94%88%E2%94%88%E2%94%88%E2%94%88%E2%94%88%E2%94%88%E2%94%A3%E2%94%81%E2%95%AF%EF%BC%8F+%0A%EF%BC%8F%EF%BC%8F%E2%94%83%E2%96%8D%E2%96%8D%E2%94%83%E2%94%88%E2%94%88%E2%94%88%E2%94%88%E2%94%88%E2%94%88%E2%94%83%EF%BC%8F%EF%BC%8F%EF%BC%8F+%0A%EF%BC%8F%EF%BC%8F%E2%95%B0%E2%94%81%E2%94%B3%E2%95%8B%E2%94%93%E2%94%8F%E2%94%81%E2%94%B3%E2%94%B3%E2%94%93%E2%94%83%EF%BC%8F%EF%BC%8F%EF%BC%8F+%0A%EF%BC%8F%EF%BC%8F%EF%BC%8F%EF%BC%8F%E2%94%97%E2%94%9B%E2%94%97%E2%94%9B%EF%BC%8F%E2%94%97%E2%94%9B%E2%94%97%E2%94%9B%EF%BC%8F%EF%BC%8F%EF%BC%8F+%0A%EF%BC%8F%EF%BC%8F%EF%BC%8F%EF%BC%8F%EF%BC%8F%EF%BC%8F%EF%BC%8F%EF%BC%8F%EF%BC%8F%EF%BC%8F%EF%BC%8F%EF%BC%8F%EF%BC%8F%EF%BC%8F%EF%BC%8F%EF%BC%8F&relids=&mode=ajax&_xiamitoken=f1feebc9c1d74f7f04a0d9fe657fba2f',
  #     success: function(res) {
  #       var res = JSON.parse(res)
  #       if (res.status === 'ok') {
  #         console.log(oid + ' 留言完毕');

  #         marked = marked + 1;

  #         if (marked === trlength) {
  #           console.log('全部留言完毕!!!');
  #         }
  #       }
  #     }
  #   })
  # }

