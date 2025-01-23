n1=input('Enter First Number')
n2=input('Enter Secon Number')
print(n1, n2)
print(type(n1))
sumation = float(n1) + float(n2)
print(sumation)

# 1. Write a program that can find area of a triangle. It should take base and height as
# an input from user and using that it should print an area of a triangle
print("This program helps you calculate an area of a triangle")
base=input("Enter base:")
height=input("Enter height:")
area=(1/2)*float(base)*float(height)
print("Area of a triangle is:",area)
# 2. Write a program that takes file name with extension as an input and
# prints just the file name without extension (you can assume that file extensions
# are always 3 character long)
file_name = input('Enter the file name qith extention')
print(file_name[:len(file_name) - 4])