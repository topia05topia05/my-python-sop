def sumArgs(*args):
    v = 0
    for i in args:
        v += i
    return v
#合計を表示
print(sumArgs(1,2,3))
print(sumArgs(1,2,3,4,5))
print(sumArgs(1,2,3,4,5,6,7,8,9,10))
