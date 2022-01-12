from random import *
import time

pin_password = input("Enter your PIN: ")
num_password = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
guess = ""
start_time = time.time()
while guess != pin_password:
    guess = ""
    for num in range(len(pin_password)):
        guess_num = num_password[randint(0, 9)]
        guess += str(guess_num)

    print(guess)

end_time = time.time()
print("Your password is : {0}".format(guess))
print("The password has been cracked in: {0}".format(end_time - start_time))
