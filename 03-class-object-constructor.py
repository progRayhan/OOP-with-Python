# class
class Students:
    # constructor
    def __init__(self,fname,lname,salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

# objects
rayhan = Students('rayhan','dollar',15000)
rafin = Students('rafin','ahmed',20000)
hridoy = Students('hridoy','islam',25000)

print(rayhan.fname)
print(rafin.salary)
print(hridoy.lname)