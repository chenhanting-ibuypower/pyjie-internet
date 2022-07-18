# Surveyed Topic

### socket & keep-alive

- What is Socket? [Link](https://www.796t.com/content/1541960708.html)
- What does Web Socket works? [Link](https://ithelp.ithome.com.tw/articles/10161110)
- The difference between socket and Keep-Alive?
- TCP / IP [Link](https://www.youtube.com/watch?v=gxoIrBFfpDU) 

### Http Request Congestion

- What is http request congestion?

  Network congestion in data networking and queueing theory is the reduced quality of service that occurs when a network node or link is carrying more data than it can handle. Typical effects include queueing delay, packet loss or the blocking of new connections. A consequence of congestion is that an incremental increase in offered load leads either only to a small increase or even a decrease in network throughput.

- The solution of HTTP request congestion? [LInk](https://blog.csdn.net/rth362147773/article/details/78453131)

### worker (gunicorn)

- The variations of performance between the numbers of workers. [Link1](https://zhuanlan.zhihu.com/p/371115835)、[Link2](https://hbnnforever.cn/article/gunicornworkers.html)
- Implementation

### Post Form

- A simple demo of transmit data via POST. [Link1](https://clay-atlas.com/blog/2020/02/25/python-flask-chinese-note-html-request-get-post/)、[Link2](https://ost.51cto.com/posts/3249)![](https://tva1.sinaimg.cn/large/e6c9d24egy1h49567tkwoj21d8078gnd.jpg)

### gil x 線程安全 x 原子操作

- 什麼是線程安全? 怎樣不安全? [link](https://zhuanlan.zhihu.com/p/42719755)

- 什麼是原子操作?  [link](https://juejin.cn/post/6844904159120998408)

- 為什麼會有GIL? [Link1](https://www.796t.com/content/1545526461.html)、[Link2](https://realpython.com/python-gil/)

- Python 的 GIL 能保證執行緒安全嗎？[LInk](https://www.zhihu.com/question/521650365)

- Python GIL 對執行緒併發性能的影響?

- Python GIL適用的時機? 有gil和沒有gil的差別? [Link](https://pythonmana.com/2022/148/202205280819525678.html)

### gevent檔案操作 x IO阻塞 x 判斷切換 x gevent.sleep()

- In what condition makes I/O congestion?  [Link](https://kknews.cc/zh-tw/code/y569jna.html)

-  What is the relationship between gevent and GIL?  [Link](https://www.programminghunter.com/article/46161044346/)

- Pros and Cons  [Link](https://www.itread01.com/article/1537412053.html)

- Python中gevent.sleep()和time.sleep()之間的區別➡️ [連結](https://www.796t.com/post/ajF3MXc=.html)

- gevent協程切換➡️ [連結](https://www.it145.com/9/24951.html)

- 對文件讀寫的gevent實作 [Link1](https://sdiehl.github.io/gevent-tutorial/)

## Implementation

This is an Simple Python Application demonstrates how to use send and receive the POST request.

### Usage

Please install `pipenv` at first, and install the packages mentioned in `requirements.txt`

```
$ pip install pipenv
$ python -m pipenv install -r requirements.txt
```

What if python could find pip

````sh
$ pip install pipenv                                                                  1 ↵
zsh: command not found: pip
````

Or execute the following command if `Pipfile` exist

```
$ python -m pipenv install --dev
```

Execute the following script to kickoff a new process.

```
$ python -m pipenv run python main.py
```

Use shell in virtual environment, and you are in the virtual environment. You don't need to add prefix `python -m pipenv run` anymore.

```
$ python -m pipenv shell
C:\path\to\your\project (main -> origin)
(yourenv-name-saqu7Akm) $
```

### Python2

In my macbook. I install `pipenv` beforehand

````sh
brew install pipenv
````

 After install the pipenv, your python version is also python2

````sh
$ python --version                                                                 
Python 2.7.16
````

Run your python

````sh
$ pipenv install -r requirements.txt 
$ pipenv shell                                                                 
Launching subshell in virtual environment...
 . /Users/chenhanting/.local/share/virtualenvs/pyjie-internet-k9c1cwxU/bin/activate
````

### Production

You can distribute an `exe` file via `pyinstaller`

```
$ python -m pipenv run pyinstaller main.py 
```

or you can distribute the file via your `.spec` file

```
$ python -m pipenv run pyinstaller --clean .\selenium-automation.spec 
```

### Prerequisite

- You should have python-3.10 in your project.
- This project is windows friendly environment. I'm not sure whether Chromedrive can work fine in MacOS system.
- [Chromedriver](https://chromedriver.chromium.org/) is included in this project. The version of chromedriver is Chrome version 102. If there is a flashback problem, you need to check your chrome version, and install a correct version of chromedriver.exe in `/driver`.