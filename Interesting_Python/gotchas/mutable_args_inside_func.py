#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Ref: 
# https://www.reddit.com/r/learnpython/comments/9oc0mu/just_an_interesting_thing_i_found/
# https://docs.python-guide.org/writing/gotchas/#mutable-default-arguments

def f(x=[]):
    return x

a = f()
b = f()
a.append(3)
b.append(4)

print(b)

# Solution 
# Ref: https://docs.python-guide.org/writing/gotchas/#mutable-default-arguments
print('\nSolving mutable argument to function gotchas')
def append_to(element, to=None):
    if to is None:
    	to = []
    to.append(element)
    return to

a = append_to(3)
b = append_to(4)
print(b)
