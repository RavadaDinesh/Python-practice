#  Global Variables
#  And also the global keyboard if you want to change a global variable inside a function
 

def myfunc():
    global x
    x = "Ice cream"

myfunc()
print("cool " + x)
print("some are very cool")

x = "Biryani -"

def myfunc():
    global x
    x = " Soop"

myfunc()
print("Delicious " + x)