import sys 
import time 

print("Запуск оС") 
time.sleep(2) 
print("Запуск...") 
time.sleep(1) 
ram1 ="16mb" 
rom1 = "95mb" 
print("RAM:" + ram1) 
print("RAM:" + rom1) 
print("CulingerOS 1.0 посденяя Версия") 
while True: 
    command1 = input("Command :") # type: ignore 
    if command1 == "systeminfo": # type: ignore 
        print("CulingerOS 1.0 посденяя Версия создатель Nufyino") 
    if command1 == "help": 
        print("Команды systeminfo калькулятор выход котик") 
    if command1 == "калькулятор": 
        wunnum = int(input("Введите первое число :"))
        oper = input("Введите / * + - :")
        twonum = int(input("Введите второе число :"))
        if oper == "+":
          print(wunnum + twonum)
          input()
        if oper == "/":
            print(wunnum / twonum)
        if oper == "*":
            print(wunnum * twonum)
        if oper == "-":
            print(wunnum - twonum)
    if command1 == "выход": 
     sys.exit()
    if command1 == "котик":
        print("𓃠 meow")
