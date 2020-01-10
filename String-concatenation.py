#String concatenation
#Type-casting 

var="Dhoni"
age=37
#print("Hello" + var + "Welcome" +age) #Integer cannot be added to string
print("Hello" + var + "Welcome") #Prints without space---> HelloDhoniWelcome
print("hello" +var+"Welcome"+str(age)) #Typecasting

#Instead of using + concatenation we can use commas ,

print("hello",var,"Welcome",age) #Perfect colution to print string & variables

#Another solution to this

print("Hello %s welcome your age is %d"%(var,age)) #Perfect 2nd solution

##    print("Hello" + var + "Welcome" +age)
##TypeError: can only concatenate str (not "int") to str

a='10'
b='20'
print(a+b) #1020
