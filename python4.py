"""
#
# Part: Python Conditions
#
"""
a = 200
b = 500
if a < b:
    print("a < b is True")
    print("a < b is True")
    print("a < b is True")
elif a > b:
    print("a > b is Ture")
elif a == b:
    print("a == b is Ture")
elif a > b:
    print("a > b is Ture")
else:
    print("Nothing")
    
if a > b: print("a > b is True")

print("A") if a < b else print("B")

a = 200
b = 50
c = 500
if (a > b) and (c > a):
    print("Both is Ture")
if a > b or a > c:
    print("Some cond is Ture")
if not (a > b):
    print("False")
if a > b:
    pass

x = 19
if x > 10:
    print("Let's go")
    if x > 20:
        print("x > 20 is Ture")
        if x > 20:
            print("Let's Ture")
            if x > 20:
                print("Let's Ture")
                if x > 20:
                    print("Let's Ture")
                

x = a + b
if c and x:
    print("1")
    
if c and (a + b):
    print("1")
