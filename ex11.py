# -*- coding: utf-8 -*-

# "," 可以使输入操作与上文打印内容在同行
print "How old are you?",
age = raw_input()

print "How tall are you?",
height = raw_input()

print "How much do you weigh?",
weight = raw_input()

print "So, you're  %r old, %r tall and %r heavy." % (age, height, weight)
