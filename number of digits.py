#number of digits
n=input("enter the string:")
a=len(n)
ch=0
for i in range(a):
    if n[i].isdigit()==1:
        ch=ch+1
print("number of digits in string",ch)        
