def split_string(function):
    def wrapper():
        fun = function()
        return fun.split()
    return wrapper



def upper_case(function):
    def wrapper():
        func = function()
        return func.upper()
    return wrapper

@split_string
@upper_case
def say_hi():
    return 'Hello narnia!'

# decorate = upper_case(say_hi)
print(say_hi())
