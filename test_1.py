

"""
Determining which option is better.
The first option is 100 dollars per day for 10 days. 
The second option is 1 dollar a day with a doubling each day for 10 days.
There are two functions that will calculate the pay rate.
function1 will be calculating the amount for the very first option, while function2 will be calculating
the amount for the second option.

function1 will output 100 x 10 days.
function2 will loop 10 times doubling the amount and add the amount to the total each time.

If the option1 is better, we will output to the user "Option 1 is better"
If the option2 is better, we will output to the user "Option 2 is better"
If the amount is equal, we will output to the user "Option 1 and Option 2 pays the same"
"""

"""

# option1
return 100 x 10

# option2
    amount = 1
    list1 = []
    loop 10x
        add amount to list1
        amount *=2
    sum = sum of all items in loop
    return amount
# main
    var1 = option1
    var2 = option2

    If var1 = var2
        "Option 1 and Option 2 pays the same"
    If var1 < var2
        "Option 2 is better"
    else
        "Option 1 is better"

main
"""

def option1():
    return 100 * 10

def option2():
    amount = 1
    list1 = []
    for i in range(0, 10):
        list1.append(amount)
        amount *=2
    # total = sum(list1)
    return total

def main():
    answer = ""
    var1 = option1() # 1000
    var2 = option2() # 1023
    
    if var1 == var2:
        answer = "Option 1 and Option 2 pays the same"
    elif var1 < var2:
        answer = "Option 2 is better"
    else:
        answer = "Option 1 is better"
    print(answer)
main()