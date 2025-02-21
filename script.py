# input salary for the month:
salary=float(input("please enter your salary for the month : ")) 

# input the name of the month you are storing the salary for:
month=str(input("please enter the name of the month you are storing the salary for : "))

# input savings:
savings=float(input("please enter the following percentages : \n \t • savings : ")) 

# input rent:
rent=float(input("\t • rent : "))

# input electricity:
electricity=float(input("\t • electricity : ")) 

#display amount allocated to savings, rent, and electricity:
savings=(salary*(savings*(10**-2)))

rent=(salary*(rent*(10**-2)))

electricity=(salary*(electricity*(10**-2)))

print("------------------------------------------------------------------------"+
    "\nthe ammount allocated to savings is :"+ str(savings) +
    "\nthe ammount allocated to rent is :"+ str(rent) +
    "\nthe ammount allocated to electricity is :"+ str(electricity))

#display total amount spent on savings, rent, and electricity combined:
total=savings+rent+electricity
print("------------------------------------------------------------------------"+
    "\nthe total amount spent on savings, rent, and electricity combined is :"+ str(total))

#display The remainder of the salary after these expenses:
remainder=salary-total
print("------------------------------------------------------------------------"+
    "\nthe remainder of the salary after the above expenses is :"+ str(remainder))

#display The monthly rent and electricity multiplied by 12 to estimate yearly rent and electricity costs.
#display total salary for the month raised to the power of 2 (just for fun).
#display Assume we save an additional random amount (e.g., $50) each month, calculate how much would be left if this amount is divided by the total amount allocated to savings. 

#Finally, the script should output all the results in a readable format.(>>>>> JUST A REMARK <<<<<<)