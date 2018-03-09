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

>>> range(10)                   # 从 0 开始到 10
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> range(1, 11)                # 从 1 开始到 11 (不包括11)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> range(0, 30, 5)             # 从 0 开始到 30 步长为 5
[0, 5, 10, 15, 20, 25]

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