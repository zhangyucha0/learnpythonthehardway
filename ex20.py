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
