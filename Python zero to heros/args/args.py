
def myfunc(a,b):
    # return 5% of a sum of a and b
    return sum((a,b))*0.05


data=myfunc(40,60)
print(data)
###########################################

def myfunc(a,b,c=0,d=0):
    return sum((a,b,c,d))*0.05

datas=myfunc(40,60,50)
print(datas)

############################################

def myfunction(*args):
    return sum(args)*0.05

data_args=myfunc(100,200,300,400)
print(data_args)