# def myfunc():
#     num = int(input("Введите число: "))
#     result = 0
#     for i in range(len(str(num))):
#         digit = num%10
#         result += digit
#         num = num//10
#     print("sum is: ", result)

# myfunc()

# def myfunc():
#     num1 = int(input("Введите число: "))
#     num2 = int(input())
#     num = str(num1) * num2
#     result = 0
#     for i in range(len(str(num))):
#         digit = int(num)%10
#         result += digit
#         num = int(num)//10
#     print(result)
#     list1 = list(map(int, str(result)))
#     summ = sum(list1)
#     print(summ)
#     list2 = list(map(int, str(summ)))
#     summ2 = sum(list2)
#     print(summ2)
    
# myfunc()

num1 = input("Введите число: ").split()
num2 = str(num1[0]) * int(num1[1])

def myfunc(num2, result = 0):
    for i in range(len(num2)):
        result = result + int(num2[i])
    
    if result > 9:
        myfunc(str(result))
    
    elif result < 10:
        print(result)

myfunc(num2)