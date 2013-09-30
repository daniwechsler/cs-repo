

def bizout (a,b):
    if b == 0:
        return (1,0)
    q   = a/b
    r   = a-q*b
    x,y = bizout(b,r)
    return (y,x-q*y)


biz = bizout(3,35)
print("%s" % format(biz))
