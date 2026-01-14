print("Please enter the Number(compare)")
a=int(input("No.1 : "))
b=int(input("No.2 : "))
c=int(input("No.3 : "))

max_value=a
if b>max_value:
    max_value=b
if c>max_value:
    max_value=c 
    
print("The Maximum is",max_value)