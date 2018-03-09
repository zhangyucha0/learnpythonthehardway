the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d" % number

# same as above
for fruit in fruits:
    print "A fruit of types: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since wo don't know what's in it
for i in change:
    print "I got %r" % i

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

# now we can print them out too
for i in elements:
    print "Element was: %d" % i
