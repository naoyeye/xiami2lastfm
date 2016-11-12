/*
* @Author: hanjiyun
* @Date:   2016-11-12 23:21:19
* @Last Modified by:   hanjiyun
* @Last Modified time: 2016-11-13 00:36:41
*/

$(document).ready(function() {

  $("#focusedInput").keydown(function(e){
    if(e.keyCode === 13){
      e.preventDefault();
      verify();
    }
  })

  $("button").click(function(e) {
    e.preventDefault();
    verify();
  });

  function verify() {
    var user = $('#focusedInput').val();
    /u\/(\d+)/.test(user);
    user = RegExp.$1;
    if (user === ''){
      alert('格式错误！');
      return 0;
    }

    $.post('/verify', {
      username: user
    }, function(data, status) {
      if (data.continued) {
        window.location.href = '/second?username=' + user;
      } else {
        alert('嘤嘤嘤，机器人已经自动为你同步咯！无需再次登录 ~~');
      }
    })
  }
});