#unit29 심사문
def calc(a,b):
    return [a+b,a-b,a*b,a/b]

#unit30 심사문
def get_min_max_score(*args):
    return [min(args),max(args)]

def get_average(**args):
    return sum(args.values())/len(args)

#unit31 심사문
def fib(n):
    if n <= 1:
        return n
    return fib(n-1)+fib(n-2)

#unit32 심사문
(list(map(lambda x : x[:x.find('.')].zfill(3)+x[x.find('.'):],files)))