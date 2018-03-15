# Learnpythonthehardway

## ex3
`print "What is 3 + 2?", 3 + 2`
`print "Is it less or equal?", 5 <= -2`


## ex4
`print "There are", cars, "cars available."`


## ex5
`print "Let's talk about %s." % my_name`

`print "He's got %s eyes and %s hair." % (my_eyes, my_hair)`

```python
# %r 打印输入的raw data（适用于debug）。
# round() 四舍五入
print '1.2 ≈ %r' % round(1.2)
```

## ex6
```python
w = "This is the left side of..."
e = "a string whith a right side."
print w + e
```

## ex7
`print "." * 10 `

## ex8
```python
# "," 可以使输入操作与上文打印内容在同行
print "How old are you?",
age = raw_input()
```

## ex9
```python
# 括号内为输入提示
age = raw_input("How old are you? ")
```

## ex10
```python
# -*- coding: utf-8 -*-

from sys import argv

# 解包。第一个参数变量(argv[0])永远为自身文件名。
script, first, second, third = argv

print "The script is called:", script
print "Your second variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
```

## ex11
```
# -*- coding: utf-8 -*-

from sys import argv

script, user_name = argv
# 定义全局输入提示符
prompt = '>'

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)
```

## ex12
查看文档
`python -m pydoc raw_input`

## ex15
不需要看那些包含 `__ `（两个下划线）的命令，这些只是垃圾而已。

## ex17
判断文件是否存在
```python
from os.path import exists

print "Does the output file exist? %r" % exists(file)
```
*tips：使用`raw_input()`暂停脚本*
```python
print "Ready, hit RETURN to continue, CTRL-C to abort."
# 这里raw_input()起到暂停脚本的作用
raw_input()
```

## ex20
`file.seek(offset, whence)`
- `offset`：开始的偏移量，也就是代表需要移动偏移的字节数

- `whence`：可选，默认值为 0。给offset参数一个定义，表示要从哪个位置开始偏移；0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。

`file.read()`：读取文件全部内容（执行完成后指针处于全文末尾）
`file.readline()`：读取单行文件内容（执行完成后指针处于行末？）
`file.readlines()`：读取全文每行的内容，已列表形式返回每行内容

读取每行内容
```python
f = open('test.txt','rU')
try: 
    for line in f:
        print line  # line带"\n"
finally:
     f.close()
```

*读取文件时，若文件执行一次读取后未关闭文件再次读取，要注意读取指针的位置*

```python
# -*- coding: utf-8 -*-

from sys import argv

script, input_file = argv


def print_all(f):
	# 读取整个文件
    print f.read()


def rewind(f):
	# 移动文件读取指针到开头 f.seek(offset, whence) whence没有设置默认为从文件开头开始（0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。）
    f.seek(0)


def print_a_line(line_count, f):
	# 读取每行（读取完该行后，读取指针停留在行结尾，因此下次再次调用此命令自动换行）
    print line_count, f.readline()

# 打开文件
current_file = open(input_file)

print "First let's print the whole file:\n"

# 读取整个文件
print_all(current_file)

print "Now let's rewind, kind of like a tape."
# 重置指针位置至内容开头（因为上步读取整个文件后读取指针处于内容末尾）
rewind(current_file)

print "Let's print three lines:"

# 打印行号
current_line = 1
# 打印行号 + 行内容
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

```

## ex24
解包
```python
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)
```

## ex25
```python
def sort_words(words):
    """Sorts the words."""
    return sorted(words)
```

## ex32

```powershell
>>> range(10)        # 从 0 开始到 10
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> range(1, 11)     # 从 1 开始到 11 (不包括11)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> range(0, 30, 5)  # 从 0 开始到 30 步长为 5
[0, 5, 10, 15, 20, 25]
```

```python# 
# we can also build lists, first start with an empty one
elements = []

elements = range(0,6)
print elements

"""
>>> range(10)                   # 从 0 开始到 10
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> range(1, 11)                # 从 1 开始到 11 (不包括11)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> range(0, 30, 5)             # 从 0 开始到 30 步长为 5
[0, 5, 10, 15, 20, 25]
"""
# then use the range function to go do 0 to 5 counts
for i in range(0,6):
    print "Adding %d to the list." % i
    # append is a function that lists Understand
    elements.append(i)
```

## ex35
`str.isdigit()` 判断字符串是否只由数字组成（不存在小数的情况）
`int(str)` 将字符串类型的数字转化为整数类型
`exit(0)` 无错误退出 
`exit(1)` 有错误退出

## ex36
1. 每一个“if 语句”必须包含一个 else. 
2. 如果这个 else 永远都不应该被执行到，因为它本身没有任何意义，那你必须在 else 语句后面使用一个叫做 die 的函数，让它打印出错误信息并且死给你看，这和上一节的习题类似，这样你可以找到很多的错误。 
3. “if 语句”的嵌套不要超过 2 层，最好尽量保持只有 1 层。 这意味着如果你在 if 里边又有了一个 if，那你就需要把第二个 if 移到另一个函数里面。 
4. 将“if 语句”当做段落来对待，其中的每一个 if, elif, else 组合就跟一个段落的句子组合一样。在这种组合的最前面和最后面留一个空行以作区分。 
5. 你的布尔测试应该很简单，如果它们很复杂的话，你需要将它们的运算事先放到一个 变量里，并且为变量取一个好名字。

## ex37
`del` del用于list列表操作，删除一个或者连续几个元素（del删除的是变量，而不是数据！）

`assert` 断言表达式。用来检查一个条件，如果它为真，就不做任何事。如果它为假，则会抛出AssertError并且包含错误信息。（可以被编译好然后从来不执行）
```python
x = 1
assert x>0, 'x is not zero or negative'
```

`yield`一个类似 return 的关键字，迭代一次遇到yield时就返回yield后面(右边)的值。重点是：下一次迭代时，从上一次迭代遇到的yield后面的代码(下一行)开始执行。

```python
#encoding:UTF-8  
def yield_test(n):  
    for i in range(n):  
        yield call(i)  
        print("i=",i)  
    #做一些其它的事情      
    print("do something.")      
    print("end.")  
  
def call(i):  
    return i*2  
  
#使用for循环  
for i in yield_test(5):  
    print(i,",")
```
输出
```
>>>   
0 ,  
i= 0  
2 ,  
i= 1  
4 ,  
i= 2  
6 ,  
i= 3  
8 ,  
i= 4  
do something.  
end.  
>>> 
```

`exec` 执行储存在字符串或文件中的Python语句，相比于 eval，exec可以执行更复杂的 Python 代码。
```python
exec "print 'hello world!'"
```

`lambda` 匿名函数
例1 获取文件扩展名
```python
_get_ext = lambda filename: os.path.splitext(filename)[-1].lower()
```
例2
```python
map( lambda x: x*x, [y for y in range(10)] )
VS
def sq(x):
    return x * x

map(sq, [y for y in range(10)])
```

`next()` 返回迭代器的下一个项目。

```python
# -*- coding: UTF-8 -*-
 
# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
        print(x)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
```
输出
```
1
2
3
4
5
```

`try` `except` `finally` 异常处理
```python
try:
     Normal execution block
except A:
     Exception A handle
except B:
     Exception B handle
except:
     Other exception handle
else:
     if no exception,get here
finally:
     print("finally")   
```

Python基本数据类型:
1. 空（None）
2. 布尔类型（Boolean）
3. 整型(Int)
4. 浮点型(Float)
5. 字符串(String)
6. 列表(List)
7. 元组(Tuple)
8. 集合(Set) *(?python2.5+)*
9. 字典(Dict)

## ex39
类中的方法（函数），第一个参数必须为`self`
```python
class Thing(object):  
    def test(self, hi):
        print self
        print "hi"

a = Thing()
print a.test("Hello")  # 实际传入两个参数，第一个参数为默认参数self
```

## ex40
字典删除key: `del key`

函数也可作为字典的`value`，如：
```python
def student(name, age):
    return name, age
    
x = {}
x['_student'] = student
print x['_student']('Ken', 12)
```
注意：
1. 上面例子函数返回的两个变量为数组形式。
2. `x['_student']`在使用前要先定义字典`x`
3. 将函数赋值给变量时函数名不加`()`

## ex42
将列表内的**字符串**（列表有且仅有字符串的情况下）以`-`作为连接符连接成一个字符串并输出
```python
stuff = ['Test', 'This', 'Out'] 
print '-'.join(stuff)
>>> Test-This-Out
```

## ex44
由于各种各样的原因，程序员将 class (类)里边的函数称作 method （方法）。很大程度上这只是个市场策略（用来推销 OOP），不过如果你把它们称作“函数”的话，是会有啰嗦的人跳出来纠正你的。如果你觉得他们太烦了，你可以告诉他们从数学方面演示一下“函数”和“方法”究竟有什么不同，这样他们会很快闭嘴的。

在你使用 class 的过程中，很大一部分时间是告诉你的 class 如何“做事情”。给这些函数命名的时候，与其命名成一个名词，不如命名为一个动词，作为给 class 的一个命令。就和 list 的 pop (抛出)函数一样，它相当于说：“嘿，列表，把这东西给我 pop 出去。”它的名字不是remove_from_end_of_list ，因为即使它的功能的确是这样，这一串字符也不是一个命令。

让你的函数保持简单小巧。由于某些原因，有些人开始学习 class 后就会忘了这一条。

你的 class 应该使用 “camel case（驼峰式大小写）”，例如你应该使用 SuperGoldFactory 而不是 super_gold_factory。

你的 __init__ 不应该做太多的事情，这会让 class 变得难以使用。

你的其它函数应该使用 “underscore format（下划线隔词）”，所以你可以写 my_awesome_hair， 而不是 myawesomehair 或者 MyAwesomeHair 。

永远永远都使用 class Name(object) 的方式定义 class，否则你会碰到大麻烦。

写注解的时候，描述清楚为什么你要这样做。代码只会告诉你“这样实现”，而不会告诉你“为什么要这样实现”，而后者比前者更重要。

## ex45
有一个重要的概念你需要弄明白，那就是“类(class)”和“对象(object)”的区别。问题在于，class 和 object 并没有真正的不同。它们其实是同样的东西，只是在不同的时间名字不同罢了

## ex46
测试库 `nose`
虚拟环境 `virtualenv`
要让文件夹被识别为项目目录，在文件夹下加入 `__init__.py`文件
断言 `assert`

简单项目骨架demo
- projecs
    - skeleton  (项目名称)
        - setup.py  (项目相关信息)
        - bin  (放脚本)
            - __init__.py
        - docs  (放文档)
        - NAME  (放核心程序)
            - __init__.py
            - xx.py
        - tests  (放测试用例)
            - __init__.py
            - xx_tests.py

## ex49
`assert_raises` 测试代码返回raises的情况
```python
from nose.tools import assert_raises

def add(x, y):
    return x + y

assert_raises(TypeError, add, 2, "0")
```

## ex50
报错1：
`AttributeError: module 'fcntl' has no attribute 'F_GETFD'`
解决1：
将`C:\Python27\fcntl.py`重命名为`fcntl_ex.py`并删除`fcntl.pyc`文件。*（建议完成相关练习后再将文件名改回）*

报错2：
`<type 'exceptions.AttributeError'> at /
No template named index`
解决2：
该问题与本书中大多数问题的原因一样，都是windows路径造成的。将`render = web.template.render('templates/')`替换为`render = web.template.render('../templates/')'`即可。

## ex52

sessions文件解码

```powershell
>>> import pickle 
>>>> import base64 
>>>> base64.b64decode(open("sessions/XXXXX").read()) "(dp1\nS'count'\np2\nI1\nsS'ip'\np3\nV127.0.0.1\np4\nsS'session_id'\np5\nS'XXXX'\np6\ns."
>>>> 
>>>> x = base64.b64decode(open("sessions/XXXXX").read()) 
>>>> 
>>>> pickle.loads(x) {'count': 1, 'ip': u'127.0.0.1', 'session_id': 'XXXXX'}
```


## 总结
本仓库中的全部脚本皆为Windows平台下编写，并且全部运行成功。

编程中遇到的大部分错误基本都是由于操作系统不同引起的文件路径格式差异问题，小部分是版本或环境差异引起的问题。

本书中文版的最新版本也是有一定年头了，而且中文版毕竟是别人翻译过来的，所以不要过于被书中的语句、案例所约束，要懂得变通。

读书过程中一定要善用搜索引擎，学会自己学习，拓展深度。

最后，将书中的一句话送给正在努力的自己和可能看到本文的你们：
*You can code. They cannot. That is pretty damn cool.*

*2018-03-15*