def select_task():
    task = input("виберіть задавдання: 1-6 ")
    match task:
        case "1":
            task1()
        case "2":
            task2()
        case "3":
            task3()
        case "4":
            task4()
        case "5":
            task5()
        case "6":
            task6()
        case "exit":
            exit()
        case _:
            print("невірний вибір, спробуйте ще раз")
            select_task()
# task 1
def task1():
    if (int(input("введіть число: ")) % 2) == 0:
        print("Even number")
    else:
        print("Odd number")
# task 2
def task2():
    if (int(input("введіть число: ")) % 7) == 0:
        print("Number is multiple 7")
    else:
        print("Number is not multiple 7") 
# task 3
def task3():
    n1 = int(input("введіть перше число: "))
    n2 = int(input("введіть друге число: "))
    if n1 > n2 and n1 != n2:
        print(f"Більше число: {n1}")
    else:
        print(f"Більше число: {n2}")
    return
# task 4
def task4():
    n1 = int(input("введіть перше число: "))
    n2 = int(input("введіть друге число: "))
    if n1 < n2 and n1 != n2:
        print(f"меньше число: {n1}")
    else:
        print(f"меньше число: {n2}")    
    return
# task 5
def task5():
    n1 = int(input("введіть перше число: "))
    n2 = int(input("введіть друге число: "))
    operation = input("яку операцію виконати: сума, різница, добуток чи середнє арифметичне ")
    match operation:
        case "сума":
            print(f"сума: {n1 + n2}")
        case "різница":
            print(f"різница: {n1 - n2}")
        case "добуток":
            print(f"добуток: {n1 * n2}")
        case "середнє арифметичне":
            print(f"середнє арифметичне: {(n1 + n2) / 2}")
        case _:
            print("невірна операція") 
# task 6
def task6():
    n1 = int(input("введіть сумму в доларах: "))
    operation = input("в яку валюту конвертувати: EUR, GBP, UAH ")
    match operation:
        case "EUR":
            print(f"сума в EUR: {n1 * 0.91}")
        case "GBP":
            print(f"сума в GBP: {n1 * 0.78}")
        case "UAH":
            print(f"сума в UAH: {n1 * 36.93}")
        case _:
            print("невірна валюта")
while True:
    select_task()