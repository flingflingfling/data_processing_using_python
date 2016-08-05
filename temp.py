#coding:utf-8

def f(n,b):
    if(n>=b):
        f(n/b,b)
    print b%b


