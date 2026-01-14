def AVG(a,b,c):
    sum=int(a)+int(b)+int(c)
    avg=sum/3
    return avg

print("Please enter the Number(Average)")
inp1=input("No.1 : ")
inp2=input("No.2 : ")
inp3=input("No.3 : ")
print("Average = ",AVG(inp1,inp2,inp3))