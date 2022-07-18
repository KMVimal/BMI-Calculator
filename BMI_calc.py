#BMI Index calculator
from tkinter import BitmapImage


weight = float(input("Enter your body weight in Kg : "))
height = float(input("Enter your height in m: "))
 
BMI = weight/(height**2)
print("Your BMI is ",int(BMI))
