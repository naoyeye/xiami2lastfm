# xiami2lastfm


<img style="max-width: 100%" src="http://ww4.sinaimg.cn/large/61b8bbf4jw1fasy3ys4onj21580nqgoh.jpg">

-----


```
cp config-example.py config.py 
```


`vim config.py`

edit `mysql_passwd`,  `API_KEY` and `API_SECRET` .

import  `scrobble.sql` into mysql.

```
mysql.server start
```


## development:

```python
python index.py
```

running on http://127.0.0.1:5000/


## production:

```
pm2 start index.py --name xiami
```