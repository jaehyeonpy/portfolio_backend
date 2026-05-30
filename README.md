```python
# creating 8000 requests at the same time,


# an example of default MongoDB, without connection pool
...
4.178138971328735
3.684394121170044
2.6561532020568848
3.19120717048645
4.187845945358276
4.73213791847229
2.616593837738037
3.240772008895874
3.1410298347473145
2.6234920024871826
4.264176845550537
2.7482240200042725
3.1747820377349854
==========
sum of elapsed_time_list: 8805.779833316803
num of elapsed_time_list(excluding error requests due to running out of ephemeral ports): 7853
avg of elapsed_time_list: 1.1213268602211643


# an example of MongoDB with connetion pool
...
0.057672977447509766
0.056729793548583984
0.056707143783569336
0.05551004409790039
0.054595232009887695
0.054277658462524414
0.053932905197143555
0.05391883850097656
0.05515003204345703
0.05338096618652344
==========
sum of elapsed_time_list: 456.9798650741577
num of elapsed_time_list(excluding error requests due to running out of ephemeral ports): 8000
avg of elapsed_time_list: 0.057122483134269715


# an example of MongoDB with connetion pool, Redis on bare-metal and with connection pool 
...
0.021188974380493164
0.020795106887817383
0.020595073699951172
0.020275115966796875
0.019960880279541016
0.01990818977355957
0.01961994171142578
==========
sum of elapsed_time_list: 27.86613392829895
num of elapsed_time_list(excluding error requests due to running out of ephemeral ports): 8000
avg of elapsed_time_list: 0.0034832667410373687


# a concurrent write lock conflict log on redis 

[INFO] 2026-05-29 15:05:29,520 proc:56930 thread:Thread-2
/Users/user/my_projects/test/portfolio_backend/core/views.py:51:get
fetched from mongodb:
{
    "_id": "LrYMUPsjtRw",
    "subtitle": "3:28:01\n않을까요? 짠. 아 사장님 한 자치하셔만 열고자\n3:28:08\n짠 파이팅 짠 저희는 공겜이 좋아서 보러온게 아니고..."
    "video_personality": "겁이 많고 쉽게 긴장하는 성격\n* 반복적으로 *“오케이 진짜 갈게요”*라고 말하면서도 실제로 나가지 못하고 주저하는 모습이 드러남.\n*..."
}
[INFO] 2026-05-29 15:05:29,520 proc:56930 thread:Thread-1
/Users/user/my_projects/test/portfolio_backend/core/views.py:51:get
fetched from mongodb:
{
    "_id": "LrYMUPsjtRw",
    "subtitle": "3:28:01\n않을까요? 짠. 아 사장님 한 자치하셔만 열고자\n3:28:08\n짠 파이팅 짠 저희는 공겜이 좋아서 보러온게 아니고..."
    "video_personality": "겁이 많고 쉽게 긴장하는 성격\n* 반복적으로 *“오케이 진짜 갈게요”*라고 말하면서도 실제로 나가지 못하고 주저하는 모습이 드러남.\n*..."
}
[ERROR] 2026-05-29 15:05:29,521 proc:56930 thread:Thread-2
/Users/user/my_projects/test/portfolio_backend/core/views.py:71:get
error:
Watched variable changed.
Traceback (most recent call last):
  File "/Users/user/my_projects/test/portfolio_backend/core/views.py", line 64, in get
    p.execute()
  File "/Users/user/my_projects/test/portfolio_backend/venv/lib/python3.9/site-packages/redis/client.py", line 1688, in execute
    return conn.retry.call_with_retry(
  File "/Users/user/my_projects/test/portfolio_backend/venv/lib/python3.9/site-packages/redis/retry.py", line 116, in call_with_retry
    return do()
  File "/Users/user/my_projects/test/portfolio_backend/venv/lib/python3.9/site-packages/redis/client.py", line 1689, in <lambda>
    lambda: execute(conn, stack, raise_on_error),
  File "/Users/user/my_projects/test/portfolio_backend/venv/lib/python3.9/site-packages/redis/client.py", line 1563, in _execute_transaction
    raise WatchError("Watched variable changed.")
redis.exceptions.WatchError: Watched variable changed.
[INFO] 2026-05-29 15:05:29,521 proc:56930 thread:Thread-1
/Users/user/my_projects/test/portfolio_backend/core/views.py:66:get
a cache set:
{
    "_id": "LrYMUPsjtRw",
    "subtitle": "3:28:01\n않을까요? 짠. 아 사장님 한 자치하셔만 열고자\n3:28:08\n짠 파이팅 짠 저희는 공겜이 좋아서 보러온게 아니고..."
    "video_personality": "겁이 많고 쉽게 긴장하는 성격\n* 반복적으로 *“오케이 진짜 갈게요”*라고 말하면서도 실제로 나가지 못하고 주저하는 모습이 드러남.\n*..."
}
```


<br>
<br>


# Notes on the codebase:
- Try-except blocks will only be used when custom error handling is needed; otherwise, exceptions will be allowed to propagate naturally.