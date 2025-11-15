# Temperature converter program.

unit = input("Is the temperature in (C)elsius, or (F)ahrenheit?: ").upper() 
temp = float(input(" Enter the temperature?: "))

if unit == "C":
    temp = round((temp * 9/5) + 32, 1)
    print(f"The temperature in fahrenheit is {temp}F")
elif unit == "F":
    temp = round((temp - 32) * 5/9, 1)
    print(f"The temperature in celsius is {temp}C")
else:
    print(f"{unit} is not a valid unit of measurement. Please use C or F next time.")