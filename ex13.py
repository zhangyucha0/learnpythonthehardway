# -*- coding: utf-8 -*-

from sys import argv

# 解包。第一个参数变量(argv[0])永远为自身文件名。
script, first, second, third = argv

print "The script is called:", script
print "Your second variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
