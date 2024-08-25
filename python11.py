"""
#
# Part: Python Try Except
#
"""
# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.
try:
    print(x)
except Exception as e :
    print("Not defind : ", e)
except Exception as e :
    print("Something else went wrong! -", e)

try:
    print("Hello Wrold")
except:
    print("Something else went wrong!")
else:
    print("Nothing went wrong!")

try:
    print(x)
except:
    print("Something else went wrong!")
finally:
    print("Fisnished!!!")

# x = -1
# if x < 10:
#     raise Exception("Sorry, number below zero")

x = "Hello"
if not (type(x) is int):
    raise TypeError("Only integers are allowed")
    