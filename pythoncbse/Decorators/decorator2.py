
def hello(show):
    print('The hello() function has been exeucted!')

    def greet():
        return 'this this greate function inside'
        show()
    def welcome():
        return 'this ithe greate function inside'

    greet()
    welcome()

@hello
def show():
    print('this is the example of decorative function')

# --------------------------------------------------------

def cool():
    def super_cool():
        return 'I am very cool!'

    return super_cool

some_func=cool()

# print(list(some_func))


# ---------------------------------------------------------------

def hello():
    return 'Hi Jose!'

def other(some_def_func):
    print('Other code runs here!')
    print(some_def_func)

other(hello)