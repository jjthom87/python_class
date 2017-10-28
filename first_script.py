Python 3.6.3 (v3.6.3:2c5fed86e0, Oct  3 2017, 00:32:08) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
1+1
2
>>> global jared
>>> jared = "hello"
>>> jared
'hello'
>>> 
'hello'
'hello'
>>> 
>>> joe = "hello"
>>> joe
'hello'
>>> import random
>>> randon.randint(10,20)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    randon.randint(10,20)
NameError: name 'randon' is not defined
>>> random.randint(10,20)
17
>>> randy = random.randint(10,20)
>>> randy
16
>>> 
>>> 
>>> 
>>> 
>>> randy
16
>>> randy
16
>>> randy
16
>>> random.randint(10,100000)
54588
>>> potionHealth = random.randint(25,50)
>>> potionHealth
46
>>> start = "I am "
>>> age = 30
>>> end = " years old"
>>> output = format(start + age + end)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    output = format(start + age + end)
TypeError: must be str, not int
>>> import format
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    import format
ModuleNotFoundError: No module named 'format'
>>> 
>>> output = start + age + end.format();
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    output = start + age + end.format();
TypeError: must be str, not int
>>> output = format(start + "{}" + end).format(age)
>>> output
'I am 30 years old'
>>> name = "Jared"
>>> age = 30
>>> place = "Jersey City"
>>> output = "Hello, my name is {} and I am {} years old. I love in {} and I love Python".format(name, age, place)
>>> output
'Hello, my name is Jared and I am 30 years old. I love in Jersey City and I love Python'
>>> print(output)
Hello, my name is Jared and I am 30 years old. I love in Jersey City and I love Python
>>> output
'Hello, my name is Jared and I am 30 years old. I love in Jersey City and I love Python'
>>> output[0:5:0]
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    output[0:5:0]
ValueError: slice step cannot be zero
>>> output[0:5:1]
'Hello'
>>> output[0:end:step]
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    output[0:end:step]
NameError: name 'step' is not defined
>>> word = "antidisestablishmentarianism"
>>> answer = word[word.index("establishment"):word.index("arianism")]
>>> answer
'establishment'
>>> word.index("establishment"):word.index("arianism")]
SyntaxError: invalid syntax
>>> word.index("establishment"):word.index("arianism")
SyntaxError: illegal target for annotation
>>> 
>>> word.index("establishment")
7
>>> clear
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
>>> email = input("What is your name").strip();
What is your namejared
>>> email
'jared'
>>> email = input("What is your name").strip();
What is your namejared@joey.com
>>> email
'jared@joey.com'
>>> user = email.index("@")
>>> user
5
>>> user = email[email.index("jared"):email.index("@")]
>>> user
'jared'
>>> user = email[:email.index("@")];
>>> user
'jared'
>>> domain = email[email.index("@"):]
>>> domain
'@joey.com'
>>> domain = email[email.index("@")+1:]
>>> domain
'joey.com'
>>> output = "Your username is {} and your domain name is {}".format(user,domain)
>>> output
'Your username is jared and your domain name is joey.com'
>>> 
=============================== RESTART: Shell ===============================
>>> 
=============================== RESTART: Shell ===============================
>>> 
