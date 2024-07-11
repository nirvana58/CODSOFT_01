def calculate(num1, num2, operator):
  if operator == "+":
    return num1 + num2
  elif operator == "-":
    return num1 - num2
  elif operator == "*":
    return num1 * num2
  elif operator == "/" and num2 != 0:
    return num1 / num2
  else:
    return None  # Handle invalid operation or division by zero

while True:
  try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Choose operation (+, -, *, /): ")
    result=calculate(num1,num2,operator)
    print(f"{num1} {operator} {num2} = {result}")

    choice=input("Do you want perform another calculation? (y/n):")
    if choice!="y":
      break
  except ValueError:
   print("invalid input")