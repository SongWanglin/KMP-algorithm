# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 10:00:38 2020

@author: 1234
"""

def P(text):
    '''
    Build prefix-suffix table for the text
    '''
    t, prefix = -1, [-1]
    for x in text:
        while t >= 0 and x!=text[t]:
            t = prefix[t]
        t += 1
        prefix.append(t)
    return prefix

def Ps(text):
    '''
    Build strong prefix-suffix table for the text
    '''
    t, prefix, length = -1, [-1], len(text)
    for i, x in enumerate(text):
        while t >= 0 and x!=text[t]:
            t = prefix[t]
        t += 1
        if i+1 < length and text[i]==text[i+1]:
            prefix.append(prefix[t])
        else:
            prefix.append(t)
    return prefix

def KMP(needle, haystack, f):
    '''
    Compute the prefix-suffix table with <f>
    '''
    prefix, length = f(needle), len(needle)
    i, pos = 0, 1 - length
    for symbol in haystack:
        while i >= 0 and needle[i]!=symbol:
            i = prefix[i]
        i += 1
        if i == length:
            yield pos
            i = prefix[length]
        pos += 1

for i in KMP('aa', 'aabaac', Ps):
    print(i)