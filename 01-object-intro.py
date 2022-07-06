class Employee:
    pass

rayhan = Employee()
ridoy = Employee()

# here, rayhan & ridoy is object name. Employee() is objects.

# add methods & attributes :
rayhan.fname = "rayhan"
rayhan.lname = "dollar"
rayhan.salary = 15000

ridoy.fname = "ridoy"
ridoy.lname = "ahmed"
ridoy.salary = 20000

print(rayhan.fname)
print(ridoy.salary)

# print object name :
print(rayhan, ridoy) # show Employee objects address.