def BMI(w,h):
    bmi= w/(h**2)
    return bmi

print("Please enter your Weight and Height")
Weight=float(input("Weight : "))
Height=float(input("Height(m=0.00) : "))
print(f"BMI is {BMI(Weight, Height):.2f}")