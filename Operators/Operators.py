# -*- coding: utf-8 -*-
"""Python Practice question on Operators of class work

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WBwr7BWcdyWIi8nqp5G26BU6hD2NJOKd

1. Take two numbers as input from the user and display their difference.
"""

num1=int(input("Enter your 1st Number = "))
num2=int(input("Enter your 2nd Number = "))
sub=(num1)-(num2)
print("Difference of two numbers is Number1",num1,"and Number2",num2,"is = ",sub )

"""2. Write a Python program to calculate the perimeter of a rectangle using the formula: perimeter = 2 * (length + width).

"""

length =int(input("Enter the length of rectangle is = "))

width =int(input("Enter the width of rectangle is = "))
print(2*(length + width))

"""3. Take a number as input from the user and display 10 times that number.

"""

number=int(input("Enter a Number = "))
result=number*10
print("The 10 time that number is = " ,result)

"""4. Write a Python program to calculate the average of four numbers entered by the user.

"""

num1=int(input("Enter your 1st Number = "))
num2=int(input("Enter your 2nd Number = "))
num3=int(input("Enter your 3rd Number = "))
num4=int(input("Enter your 4th Number = "))

average=(num1+num2+num3+num4)/4
print("The average of the 4 numbers is",num1,num2,num3,"and",num4,"is = ",average4)

"""5. Write a Python program to swap two numbers using a temporary variable."""

num1=int(input("Enter your 1st Number = "))
num2=int(input("Enter your 2nd Number = "))
print("Before swapping two number is = ",num1,num2)
temp=num1
num1=num2
num2=temp
print("After swapping two number is = ",num1,num2)

"""6. Take three numbers as input from the user and display their sum and product.

"""

num1=int(input("Enter your 1st Number = "))
num2=int(input("Enter your 2nd Number = "))
num3=int(input("Enter your 3rd Number = "))
sum=num1+num2+num3
product=num1*num2*num3
print("The sum of three numbers is",num1,num2,num3,"is = ", sum)
print("The product of three numbers is",num1,num2,num3,"is = ", product)

"""7. Write a Python program to take two numbers as input and display the result of their multiplication.

"""

num1=int(input("Enter your 1st Number = "))
num2=int(input("Enter your 2nd Number = "))
mul=num1*num2*num3
print("The multiplication. of three numbers is",num1,num2,num3,"is = ", mul)

"""8. Take two numbers as input and display the result of their subtraction.

"""

n1=int(input("Enter your 1st Number = "))
n2=int(input("Enter your 2nd Number = "))
sub=n1-n2
print("The multiplication. of three numbers is",n1,n2,"is = ", sub)

"""9. Write a Python program to find the result of dividing two numbers and display the quotient only.

"""

numerator=int(input("enter the 1st number = "))
denometor=int(input("enter the 2nd number = "))
quotient=numerator//denometor
print("the quotient is = " ,quotient)

"""10. Take two numbers as input and display the result of their modulus operation (remainder).

"""

n1=int(input("Enter your 1st Number = "))
n2=int(input("Enter your 2nd Number = "))
modulus_operation= n1%n2
print("modulus_operation is = ",modulus_operation)

"""11. Write a Python program to calculate the simple interest using the formula: SI = (P * R * T) / 100.

"""

principle=float(input("Enter the principle amount is = "))
rate =int(input("Enter the rate of the interest is = "))
time=int(input("Enter  the time ="))
simple_interest =(principle*rate*time)/100
print("Simple interest is = ", simple_interest )

"""12. Take the radius as input and calculate the circumference of a circle using the formula: C = 2 * π * r (use 3.14159 for π).
\
"""

radius =int(input("Enter the radius is = "))
circumference= 2*3.14159*radius
print(circumference)

"""13. Write a Python program to calculate the area of a square using the formula: area = side * side.

"""

side1=int(input("Enter the first side of the area is = "))
side2=int(input("Enter the second side of the area is = "))
area=side1*side2
print("Area of the square is = ",area)

"""14. Take two numbers as input and display their exponential result using the power operator (**).


"""

n1=int(input("Enter the first number is = "))
n2=int(input("Enter the second number is = "))
exponential=n1**n2
print(exponential)

"""15. Write a Python program to calculate the area of a circle using the formula: area = π * r^2.


"""

radius=int(input("Enter the radius of the area is = "))
area=3.14*radius**2.
print(area)

"""16. Take the base and exponent as input and display the result of base raised to the exponent.

"""

base=int(input("Enter the base number is = "))
exponent=int(input("Enter the exponent number is = "))
result=base**exponent
print(result)

"""17. Write a Python program to convert an amount in kilometers to meters (1 km = 1000 meters).

"""

kilometers=int(input("Enter the amount in  kilometers is = "))
meters=kilometers*1000
print("Convert the amount in kilometers  to meters  ",kilometers," is = ",meters)

"""18. Take a number as input and display whether it is an even or odd number using modulus (%).

"""

number=int(input("Enter the number is = "))
if number % 2==0:
  print("The Given number is Even = ",number)
else:
   print("The Given number is old = " ,number)

"""19. Write a Python program to calculate the total price of items where the price per item and number of items are provided by the user.

"""

item1=int(input("Enter the price of item1 is = "))
qty1=int(input("Enter the Quantity  of item1 is = "))

item2=int(input("Enter the price of item2 is = "))
qty2=int(input("Enter the Quantity of item2 is = "))
total_price1 =(item1*qty1)
total_price2 =(item2*qty2)
print("The total price of the ", item1,"is = ",total_price1)
print("The total price of the ", item2,"is = ",total_price2)

"""20. Take three numbers as input from the user and display the result of multiplying the first number by the sum of the second and third numbers.

"""

num1=int(input("Enter your 1st Number = "))
num2=int(input("Enter your 2nd Number = "))
num3=int(input("Enter your 3rd Number = "))
mul=(num1*(num2+num3))

print(mul)

"""21. Take the radius as input and calculate the circumference of a circle using the formula: C = 2 * π * r (use 3.14159 for π).

"""



radius=int(input("Enter the radius is = "))
circumference=2 * 3.14159 * radius
print(circumference)

"""22. Write a Python program to calculate the area of a square using the formula: area = side * side.

"""

side1=int(input("Enter the first side of the area is = "))
side2=int(input("Enter the second side of the area is = "))
area=side1*side2
print("Area of the square is = ",area)

"""23. Take two numbers as input and display their exponential result using the power operator (**).

"""

n1=int(input("Enter the first number is = "))
n2=int(input("Enter the second number is = "))
exponential=n1**n2
print(exponential)

"""24. Write a Python program to calculate the area of a circle using the formula: area = π * r^2.

"""

radius=int(input("Enter the radius of the area is = "))
area=3.14*radius**2.
print(area)

"""25. Take the base and exponent as input and display the result of base raised to the exponent.

"""

base=int(input("Enter the base number is = "))
exponent=int(input("Enter the exponent number is = "))
result=base**exponent
print(result)

"""26. Write a Python program to convert an amount in kilometers to meters (1 km = 1000 meters).

"""

kilometers=int(input("Enter the amount in  kilometers is = "))
meters=kilometers*1000
print("Convert the amount in kilometers  to meters  ",kilometers," is = ",meters)

"""27. Take a number as input and display whether it is an even or odd number using modulus (%).

"""

number=int(input("Enter the number is = "))
if number % 2==0:
  print("The Given number is Even = ",number)
else:
   print("The Given number is old = " ,number)

"""28. Write a Python program to calculate the total price of items where the price per item and number of items are provided by the user.

"""

item1=int(input("Enter the price of item1 is = "))
qty1=int(input("Enter the Quantity  of item1 is = "))

item2=int(input("Enter the price of item2 is = "))
qty2=int(input("Enter the Quantity of item2 is = "))
total_price1 =(item1*qty1)
total_price2 =(item2*qty2)
print("The total price of the ", item1,"is = ",total_price1)
print("The total price of the ", item2,"is = ",total_price2)

"""29. Take three numbers as input from the user and display the result of multiplying the first number by the sum of the second and third numbers.

"""

num1=int(input("Enter your 1st Number = "))
num2=int(input("Enter your 2nd Number = "))
num3=int(input("Enter your 3rd Number = "))
mul=(num1*(num2+num3))

print(mul)

"""30. Write a Python program to calculate the speed using the formula: speed = distance / time.

"""

distance=int(input("Enter the Distance is = "))
time=int(input("Enter the time = "))
speed = distance / time
print("the speed is = ",speed)