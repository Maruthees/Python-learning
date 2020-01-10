

path="C:\newfolder\time.tat"
print(path)

#python takes the literal as \n -newline \t as tab to avoid this use Raw data for all strings


path=r"C:\newfolder\time.tat"  #before string use the word r
print(path)


#multi line triple characters, looks for next line untill the quotes are matched

path='''india is my
          country'''
print(path)



data=" india "
print(data)
print(len(data))
data=data.strip()  #Strip removes the unwanted spaces before & after the string
print(data)
print(len(data))


data="@@india@@"
print(data)
print(len(data))
data=data.strip('@')  #Strip removes the unwanted spaces before & after the string
print(data)
print(len(data))


#rstrip removes the spaces or define characters at the right hand side only
#lstrip removes the spaces or defined characters at the left hand side only


data="@@india@@"
print(data)
print(len(data))
data=data.rstrip('@')  #Strip removes the unwanted spaces before & after the string
print(data)
print(len(data))



data="@@india@@"
print(data)
print(len(data))
data=data.lstrip('@')  #Strip removes the unwanted spaces before & after the string
print(data)
print(len(data))
