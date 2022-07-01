# function decorators, class decorators

# 1.function decorators: function another function as argument
# allows to add new functionality of order function
# @mydecorator
# def dosomething():
#    pass
import functools


def start_end_decorator(func):

    # allow paramerters
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result

    return wrapper


# Extends the functionality by adding decoratrors
@start_end_decorator
def print_name():
    print("Alex")


print_name()


@start_end_decorator
def add5(x):
    print(x + 5)
    return x + 5


add5(10)

# print(help(add5))
print(add5.__name__)

# decoratros with arguments
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator_repeat


@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")


greet("Bob")

# nested decorators are like { { { } } }


class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"This is executed {self.num_calls} times")
        return self.func(*args, **kwargs)


# class decoratros - usually to update the state
@CountCalls
def say_hello():
    print("Hello")


say_hello()
say_hello()

#typical implementation of decoratros
# debug, checks, time, registration of function, cache the return value, update the state
