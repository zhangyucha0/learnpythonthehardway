# -*- coding: utf-8 -*-

from sys import argv
from os.path import exists

# 解包
script, from_file, to_file = argv

# 打印输入输出文件名
print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
# 打开源文件
input = open(from_file)
# 读取源文件全部内容
indata = input.read()

# 打印源文件内容长度
print "The input file is %d bytes long" % len(indata)

# 打印语句，提示目标文件是否存在
print "Does the output file exist? %r" % exists(to_file)
# 打印语句，提示如何继续，如何退吹
print "Ready, hit RETURN to continue, CTRL-C to abort."
# 这里raw_input()起到暂停脚本的作用
raw_input()

# 打开目标文件
output = open(to_file, 'w')
# 将源文件的内容写入目标文件
output.write(indata)

# 打印语句提示操作执行完毕
print "Alright, all done."

# 关闭源文件
output.close()
# 目标文件
input.close()
