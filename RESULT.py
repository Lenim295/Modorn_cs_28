def HELLO():
    print("hello Student!")

def SUM_2_NUMBER():
    print("Please enter the Number(A+B)")
    A=input("A : ")
    B=input("B : ")
    sum=int(A)+int(B)
    print(f"SUM = {sum} ")

def REC():
    print("Please enter the Number(Rectangle)")
    W=input("W : ")
    H=input("H : ")
    R=int(W)*int(H)
    print(f"Rectangle Area is {R}")

def AVG():
    print("Please enter the Number(Average)")
    a=input("No.1 : ")
    b=input("No.2 : ")
    c=input("No.3 : ")
    sum=int(a)+int(b)+int(c)
    avg=sum/3
    print(f"Average = {avg}")

def FAH():
    c=float(input("Celsius c : "))
    fah=float((c*(9/5))+32)
    print(f"Fahrenheit f = {fah} ")

def EVEN_ODD():
    x=float(input("Please enter the Number : "))
    if x%2==0:
        print("Number is Even Number")
    else:
        print("Number is Ood Number")

def POSI_NEGA_ZERO():
    x=int(input("Please enter the Number : "))
    if x>0:
        print("Number is Positive")
    elif x==0:
        print("Number is Zero")
    else:
        print("Number is Negative")

def MAXI():
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

def DISCOUNT():
    p=float(input("Please enter the price : "))
    if p>=1000:
        Dis=(p*(100-10))/100
        print("After Discount (10%) :",Dis)
    else:
        print("No Discount")

def BMI():
    print("Please enter your Weight and Height")
    W=float(input("Weight : "))
    H=float(input("Height(m=0.00) : "))
    bmi= W/(H**2)
    print(f"BMI is {bmi:.2f}")

def show_menu():
  print("\n====รายการ====")
  print("1) hello")
  print("2) Sum of Two Numbers")
  print("3) Rectangle Area")
  print("4) Average of 3 Scores")
  print("5) Temperature Convert ")
  print("6) Even or Odd")
  print("7) +/-/0")
  print("8) Max of Three")
  print("9) Discount")
  print("10) BMI")

def main():
  while True:
    show_menu()
    operate=input("กรุณาเลือกรายการ :")
    if(operate=="1"):
        HELLO()
    elif(operate=="2"):
        SUM_2_NUMBER()
    elif(operate=="3"):
        REC()
    elif(operate=="4"):
        AVG()
    elif(operate=="5"):
        FAH()
    elif(operate=="6"):
        EVEN_ODD()
    elif(operate=="7"):
        POSI_NEGA_ZERO()
    elif(operate=="8"):
        MAXI()
    elif(operate=="9"):
        DISCOUNT()
    elif(operate=="10"):
        BMI()
    elif(operate=="0"):
        print("ออกจากรายการ")
        break
    else:
        print("Not Found")


main()
