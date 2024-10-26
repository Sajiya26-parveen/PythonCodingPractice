#Reverse a string
def reverse(str):
    new_str=''
    i=len(str)-1
    while i>=0:
        new_str+=str[i]
        i-=1
    return new_str
str= input("\n enter the string:")
print("\n the reversed string is:", reverse(str))