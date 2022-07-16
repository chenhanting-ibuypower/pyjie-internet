# Surveyed Topic

### socket.keep-alive

(1) What is Socket?

(2)[TCP連線、Socket連線、Http連線的區別?](https://www.796t.com/content/1541960708.html)

https://www.796t.com/content/1541960708.html

(3) Web Socket如何運作？

https://ithelp.ithome.com.tw/articles/10161110

(4)socket和Keep-Alive的區別?

 

補充:

(1) 網路七層與TCP/IP

https://www.youtube.com/watch?v=gxoIrBFfpDU

 

### HTTP阻塞

(1)什麼是HTTP請求阻塞?

(2)HTTP請求阻塞解決方法?

https://blog.csdn.net/rth362147773/article/details/78453131

 

### worker工作者 (gunicorn)

(1) workers 的數量與性能的變化

https://zhuanlan.zhihu.com/p/371115835

https://hbnnforever.cn/article/gunicornworkers.html

(2)實作worker數量變化

 

### post表單

(1)簡易傳送資料的POST實例

https://clay-atlas.com/blog/2020/02/25/python-flask-chinese-note-html-request-get-post/

https://ost.51cto.com/posts/3249

 

 

### gil x 線程安全 x 原子操作

- 什麼是線程安全?怎樣不安全?

https://zhuanlan.zhihu.com/p/42719755

- 什麼是原子操作?

https://juejin.cn/post/6844904159120998408

- 為什麼會有GIL?

https://www.796t.com/content/1545526461.html

https://realpython.com/python-gil/

- Python 的 GIL 能保證執行緒安全嗎？

https://www.zhihu.com/question/521650365

- Python GIL 對執行緒併發性能的影響?

- Python GIL適用的時機? 有gil和沒有gil的差別?

https://pythonmana.com/2022/148/202205280819525678.html

### gevent檔案操作 x IO阻塞 x 判斷切換 x gevent.sleep()

- 什麼情況造成IO阻塞? ➡️ [連結](https://kknews.cc/zh-tw/code/y569jna.html)

-  gevent與GIL的關係? ➡️ [連結](https://www.programminghunter.com/article/46161044346/)

- 使用的優缺點 ➡️ [連結](https://www.itread01.com/article/1537412053.html)

- Python中gevent.sleep()和time.sleep()之間的區別➡️ [連結](https://www.796t.com/post/ajF3MXc=.html)

- gevent協程切換➡️ [連結](https://www.it145.com/9/24951.html)

- 對文件讀寫的gevent實作



This is an IBupower Scraper Application implemented with python.

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

How you can do with pipenv

````
Usage Examples:
   Create a new project using Python 3.7, specifically:
   $ pipenv --python 3.7

   Remove project virtualenv (inferred from current directory):
   $ pipenv --rm

   Install all dependencies for a project (including dev):
   $ pipenv install --dev

   Create a lockfile containing pre-releases:
   $ pipenv lock --pre

   Show a graph of your installed dependencies:
   $ pipenv graph

   Check your installed dependencies for security vulnerabilities:
   $ pipenv check

   Install a local setup.py into your virtual environment/Pipfile:
   $ pipenv install -e .

   Use a lower-level pip command:
   $ pipenv run pip freeze

Commands:
  check         Checks for PyUp Safety security vulnerabilities and against
                PEP 508 markers provided in Pipfile.
  clean         Uninstalls all packages not specified in Pipfile.lock.
  graph         Displays currently-installed dependency graph information.
  install       Installs provided packages and adds them to Pipfile, or (if no
                packages are given), installs all packages from Pipfile.
  lock          Generates Pipfile.lock.
  open          View a given module in your editor.
  requirements  Generate a requirements.txt from Pipfile.lock.
  run           Spawns a command installed into the virtualenv.
  scripts       Lists scripts in current environment config.
  shell         Spawns a shell within the virtualenv.
  sync          Installs all packages specified in Pipfile.lock.
  uninstall     Uninstalls a provided package and removes it from Pipfile.
  update        Runs lock, then sync.
  verify        Verify the hash in Pipfile.lock is up-to-date.
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