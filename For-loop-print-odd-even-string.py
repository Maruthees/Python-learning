#printing the odd & even place string

oddvar=""
evenvar=""

x="doni is cool"
print(x)
for i,j in enumerate(x):
    if i%2!=0:
        print("Odd value")
        j=j.upper()
        print(j)
        oddvar+=j

    else:
        print("Even values")
        j=j.upper()
        print(j)
        evenvar+=j


print ("Even var",evenvar)
print("Odd var",oddvar)
        
