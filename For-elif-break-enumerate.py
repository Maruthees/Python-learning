
#break is for for-loop where it comes out of loop immediately

x="Dhoni is captain"

for i in x:
    if i=='i':
        print("Sucess")
        break
    else:
        print("Fail")

#To check more conditions use elif


for i in x:
    if i=='i':
        print("Success we got i")

    elif i=='a':
        print("Sucess we got a")
    else:
        print("Fail")


#logical operators use instead of elif
print("Logical operators")
for i in x:
    if i=='i' or i=='a':
        print("Success we got i OR a")
    else:
        print("Fail")
        
#Enumerate provides index & values
#check enumerate
for i in enumerate(x):
    print(i)


#Checking enumerate
for i in enumerate(x):
    if i=='i':
        print('sucess')
    else:
        print('Fail')

#Since enumerate return index & values we need to use two values for index & values

for i,j in enumerate(x):
    print(i ,j)




        
    


    
