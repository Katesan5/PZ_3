def subst(a,b):
    print("a-b = ", a-b)
def summ(x,y):
    print("x+y = ", x+y)
def decore(func):
    def wrapper(t,z):
        print("Run function")
        func(t,z)
        print("Stop function")
    return wrapper
subst_wrapped = decore(subst)
summ_wrapped = decore(summ)
subst(88,77)
summ(88, 77)
subst_wrapped(88, 77)
summ_wrapped(88, 77)