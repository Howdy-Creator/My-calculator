#calculator
from random import randint
from colorama import Fore, Back, Style
from colorama import init
init()
variables = {"sign" : "+","num_1" : 0,"num_2" : 0, "equally" : 0};
variables2 =[0, 1, 2, 3, 4, 5]
right = True
strings = [ 
	["Welcome in cool calculator!", "Hello",
	 "Hi from the calculator!",
	  "Little Hi from the calculator!"],
	   ["Choose, what you want to do? ",
	   "What we want do? ", "+ - * or /? "],
	   ["Enter first integer ", "Please enter first int ",
	    "Enter second integer ", "Ok, now enter second int ",
	     "Where is second int??? "],
	   ["Wow! Your result is: ",
	    "Look! It's your result: ", "Your result is: "],
	    ["Oops! you entered a sign I don't know!",
	    "Wrong sign, try again",
	    "I don't understand the sign you entered"]
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
rand_set(0,0,3);
print(Back.YELLOW)
print(strings[0][variables2[0]])
rand_set(1,0,2)
print(Back.RESET)
print(Fore.GREEN)
rand_say("sign", 1, 1)

if (variables["sign"] == "+"):
	cho = lambda x , y: x + y
elif (variables["sign"] == "-"):
	cho = lambda x , y: x - y
elif (variables["sign"] == "*"):
	cho = lambda x , y: x * y
elif (variables["sign"] == "/"):
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
	variables["equally"] = cho(int(variables["num_1"]), int(variables["num_2"]))
	rand_set_and_say(4,0,2,3);
	print(Fore.RED)
	print(variables["equally"])