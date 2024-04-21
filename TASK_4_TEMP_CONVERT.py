#Create a program that allows the user to convert temperatures between Fahrenheit and Celsius

#Enter the Temperature in Celsius
Celsius = int(input("Enter the Temperature in Celsius : "))

#Convert it into Fahrenheit
F = (Celsius * 9 / 5 ) + 32

print("The Temperature in Fahrenheit is : ", F)

#Also Convert from Fahrenheit to Celsius
Fahrenheit = ("Enter the Temperature in Fahrenheit : ")

#Convert it into Celsius
C = (F - 32) * 5 / 9

print("The Temperature in Celsius is : ", C)