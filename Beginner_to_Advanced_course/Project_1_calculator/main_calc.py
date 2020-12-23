import re

previous = 0
run = True

print("Magical calculator")
print("Type 'Quit' to exit\n")

a = 6
while run:
    equation = input("Enter equation:")
    if equation == "Quit":
        run = False
    else:
        equation = re.sub("[a-zA-Z,.()" "]", "", equation)
        equation = eval(equation) + previous
        previous = equation
    print(equation)

