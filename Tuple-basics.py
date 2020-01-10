

#Tuple belongs to immutable , cannot be modified

var=('dhoni','kohli')
print(type(var))

tuple1=('dhoni') #This is not a tuple it becomes a string
#Solution is to have a comma

print(type(tuple1))


tuple2=('dhoni',)#Declare a tuple with single argument and give a comma
print(type(tuple2))
#Append generally looks for a comma at the end ,


##new=[ ,'b']
##new.append('c')
##print(new)

#List of lists

temp=[['a','b'],['c',3]]
print(temp[1][1])
print(type(temp[1][1]))
