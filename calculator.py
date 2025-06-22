print("Калкулятор")
print("Доступные операции (+,-,*,/)")

num1 = int(input("Введите 1-е число: "))
num2 = input("Введите операцию (+,-,*,/): ")
num3 = int(input("Введите 2-е число: "))

if num2 == "+":
    result = num1 + num3
    print("Результат: ", result)
elif num2 == "-":
    result = num1 - num3
    print("Результат: ", result)
elif num2 == "*":
    result = num1 * num3
    print("Результат: ", result)
elif num2 == "/":
    if num3 == 0:
        print("Ошибка деления на 0!")
    else:
        result = num1 / num3
        print("Результат: ", result)
else:
    print("Ошибка, что-то пошло не так...")
