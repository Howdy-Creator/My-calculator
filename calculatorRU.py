#дебильный калькулятор
from random import randint
from colorama import Fore, Back, Style
from colorama import init
init()
variables = {"znak" : "+","num_1" : 0,"num_2" : 0, "ravno" : 0};
variables2 =[0, 1, 2, 3, 4, 5]
right = True
strings = [ 
	["Добро пожаловать в крутой калькулятор!", "Здравствуй!",
	 "Привет из калькулятора!",
	  "Приветик от калькулятора!"],
	   ["Выбери, что будешь делать? ",
	   "какой знак мы будем делать? ", "+ - * или /? "],
	   ["Введи первое число ", "пожалуйста введи первое число ",
	    "Введи второе число ", "Так, а теперь второе число ",
	     "Ну а второе число? "],
	   ["Ого! Твой результат равен: ",
	    "Смотри! Это твой результат: ", "Твой результат: "],
	    ["Упс, ты ввел знак который я не знаю, повтори ещё раз?",
	    "Не правельный знак, повтори попытку",
	    "Что то я не понял знака который ты ввел"]
	   ]
#----------------------------------------------------------

cho = lambda x , y: x + y
nl = lambda : print('--------------------------------')
def rand_set (num, start, end):
	variables2[num] = randint(start,end)
	pass
def rand_set_and_say (num, start, end, String_num):
	variables2[num] = randint(start,end)
	print(strings[String_num][variables2[num]])
	pass
def rand_say (string, String_num,Variables2_num):
	variables[str(string)] = input(strings[String_num][variables2[int(Variables2_num)]]);
	pass
#----------------------------------------------------------
#variables2[0] = randint(0,3);
rand_set(0,0,3);
print(Back.YELLOW)
print(strings[0][variables2[0]])
#variables2[1] = randint(0,1)
rand_set(1,0,2)
#variables["znak"] = input(strings[1][variables2[1]])
print(Back.RESET)
print(Fore.GREEN)
rand_say("znak", 1, 1)

if (variables["znak"] == "+"):
	cho = lambda x , y: x + y
elif (variables["znak"] == "-"):
	cho = lambda x , y: x - y
elif (variables["znak"] == "*"):
	cho = lambda x , y: x * y
elif (variables["znak"] == "/"):
	cho = lambda x , y: x / y
else:
	print(Fore.RESET)
	print(Fore.RED)
	rand_set_and_say(5,0,2,4);
	right = False
	print(Style.RESET_ALL)

if (right == True):
	print(Back.WHITE)
	print(Fore.BLACK)
	rand_set(2,0,1);
	rand_say("num_1",2,2);
	rand_set(3,2,4);
	rand_say("num_2",2,3);
	nl()

	print(Back.RESET)
	print(Fore.RESET)
	print(Fore.CYAN)
	variables["ravno"] = cho(int(variables["num_1"]), int(variables["num_2"]))
	rand_set_and_say(4,0,2,3);
	print(Fore.RED)
	print(variables["ravno"])