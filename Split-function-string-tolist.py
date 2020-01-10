
#convert string to list , this is done by removing spaces using split function

var="dhoni     is my captain"

output=var.split()
print(output)

#Splitting based on the values given , split can be with argument or without argument
#split everywhere when i is found
output1=var.split('i')
print(output1)

#split only two times
output2=var.split('i',2)
print(output2)


#If the var is not going to be used anywhere alse use the same var to store after split operation

var=var.split()
print(var)




 
