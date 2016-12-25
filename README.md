# xiami2lastfm


<img style="max-width: 100%" src="http://ww4.sinaimg.cn/large/61b8bbf4jw1fasy3ys4onj21580nqgoh.jpg">

-----


```bash
cp config-example.py config.py 
```


`vim config.py`

edit `mysql_passwd`,  `API_KEY` and `API_SECRET` .

import  `scrobble.sql` into mysql.

```bash
mysql.server start
```


## development:

```bash
python index.py
```

running on http://127.0.0.1:5000/


## production:

```bash
pm2 start index.py --name xiami
```

----

restart:

```bash
pm2 restart index.py --update-env
```

## 部署备忘：

阿里云上用 python 启动：端口 5000（调试用）：

```bash
python index.py --host 127.0.0.1 --port 5000
```

直接访问 123.57.21.239:5000 是不行的。通过 linode 的 nginx 指向了阿里云 nginx 80 端口，aliyun nginx 监听 80 端口，然后再指向 5000 ，流程：

http://xiami2lastfm.han.im/ => 123.57.21.239:80 => 123.57.21.239:5000

## 报错：

```bash
[root@iZ25677w1axZ xiami2lastfm]# nginx -s reload
nginx: [error] invalid PID number "" in "/run/nginx.pid"
```

解决：

```bash
/usr/sbin/nginx -c /etc/nginx/nginx.conf
```
