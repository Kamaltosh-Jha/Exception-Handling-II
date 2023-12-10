# a) Our own class
class NotArmstrongError(Exception):

    def __init__(self, value) -> None:
        self.value = value

    def __str__(self) -> str:
        return(repr(self.value))


while(True):
    # b) Try, Except, Else, Finally
    try:
        # number entered by the user
        number = int(input("Enter your number to check! \n")) 

        # number of digits
        n = len(str(number)) 
        
        sum = 0
        for i in str(number):
            sum += int(i)**n

        if sum != number:
            raise NotArmstrongError(number)

    except ValueError as val_err:
        print("Please enter a number!")
        print(val_err)
        continue
    except NotArmstrongError as arm_err:
        print('''Unfortunately, It is not an Armstrong Number''')
        print("Your number was", arm_err)
    else:
        print("Congratulations")
        print(f"{number} is an Armstrong Number")
    finally:
        print("Check Complete!")
       

    choice = int(input("Do you want to test another number? Enter 1 for Yes, and 0 for No\n"))
    if (choice == 1):
        continue
    else:
        break

print("Thank you and Good Bye!")

'''
Output of Program 1

Enter your number to check! 
370
Congratulations
370 is an Armstrong Number
Check Complete!
Do you want to test another number? Enter 1 for Yes, and 0 for No
1
Enter your number to check! 
360
Unfortunately, 
              It is not an Armstrong Number
Your number was 360
Check Complete!
Do you want to test another number? Enter 1 for Yes, and 0 for No
1
Enter your number to check! 
abcd
Please enter a number!
invalid literal for int() with base 10: 'abcd'
Check Complete!
Enter your number to check!
67
Unfortunately,
              It is not an Armstrong Number
Your number was 67
Check Complete!
Do you want to test another number? Enter 1 for Yes, and 0 for No
0
Thank you and Good Bye!

'''