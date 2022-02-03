#Write a Python function to find the Max of three numbers.

# num1 = int(input("please enter the first number: "))
# num2 = int(input("please enter the second number: "))
# num3 = int(input("please enter the third number: "))

# def findmax(num1, num2, num3):
#     list = [num1, num2, num3]
#     top = max(list)
#     return top

# A = findmax(num1, num2, num3)
# print(A,"is the highest number")

#Write a Python function to sum all the numbers in a list

# num = []
# while len(num) < 5:
#     num.append(int(input("please enter a number: ")))

# def calc(num):
#     result = sum(num)
#     return result

# res = calc(num)
# print(num,"=",res)

#Write a Python function to multiply all the numbers in a list.

# num = []
# while len(num) < 5:
#     num.append(int(input("please enter a number: ")))

# def calc(num):
#     result = 1
#     for n in num:
#         result = result * n
#     return result

# res = calc(num)
# print(res)

#Write a Python function that takes a number as a parameter and check the number is prime or not

# num = int(input("insert number to test: "))

# def prime(num):
#     if num ==1:
#         return False
#     elif num == 2:
#         return True
#     elif num%2==0:
#         return False
#     else:
#         for x in range(3,num,2):
#             if (num % x==0):
#                 return False
#         return True

# result = prime(num)
# print(num,"is prime?", result) 

#Write a Python program to print the even numbers from a given list

num = []
count = 0
while len(num) < 25:
    num.append(int(input("please insert a number: ")))
    while count < 25:
        num.append(num[-1] + 1)
        count = count + 1

def evens(num):
    even = []
    for n in num:
        if n %2 == 0:
            even.append(n)
    return even

result = evens(num)
print(num)
print(result)

