# a generator code for fibonacci number


def genreate_fibonacci():
    n1 = 0
    n2 = 1
    while (1):
        yield n1
        n1, n2 = n2, n1+n2 

seq = genreate_fibonacci()

print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))


#iterator code by class

class Find_fib:

    def __init__(self,max1):
        pass
    
    def __iter(self):
        yield self

    def __next__


    
