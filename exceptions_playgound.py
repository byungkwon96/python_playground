# Errors and exceptions

# syntax Error
# too many parantese or not written right
# a =5 print(a)

# type error - type is not consistence
# a = 5 + '10'

# import error - import something doesn't exist

# name error - not defined error

# file error -file doesn't exist

# value eror - right type but invalue value
# a = [1,2,3]
# a.remove(4)
# --- 4 doesn't exist

# index error - index doesn't exist in the list out of range

# can raise the error with the raise keyword
x = -5
if x < 0:
    raise Exception("x should be positive")

# can assert
assert x >= 0, "x is not positive"

# handle exception
try:
    a = 5 / 0
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print("an error happened")
    print(e)
# runs when no exception
else:
    print("everything is fine")
# runs always used to make cleanup operation
finally:
    print("cleaning up")

# define own error subclass of Exception class
class ValueTooHighError(Exception):
    pass


class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def test_value(x):
    if x > 100:
        raise ValueTooHighError("value is too high")
    if x < 5:
        raise ValueTooSmallError("value too small", x)


try:
    test_value(200)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)