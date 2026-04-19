n =input("tell me your name: ")
def greet(name):
    return f"Hello {name}"

message = greet(n)
print(message)

z = int(input("Enter the first number: "))
x = int(input("Enter the second number: "))
u = input("Enter the operator: ")
def calc(a,b):
    if u == "+" :
        return a+b
    if u == "*" :
        return a*b
    else:
        print("Invalid operator")

result = calc(z,x)
print(result)
