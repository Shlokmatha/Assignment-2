num1 = int(input("Enter the first number: \n \t ")) 
num2 = int(input("Enter the second number: \n \t ")) 
# Using XOR function
a = bin(num1^num2) 
print(bin(num1))
print(bin(num2))
print(a)
b = a.count('1')
print(b)