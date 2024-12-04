import time
print('Please insert your ATM Card')
time.sleep(5)
pin=int(input('Enter you 4 digit ATM Pin'))
balance=2000
if pin==1234:
    while True:
        print('1=Check Balance')
        print('2=Withdraw Amount')
        print('3=deposit Amount')
        print('4=Exit')
        try:
            option=int(input('Choose any option above'))
        except:
            print('Please choose the valid option')
        if option==1:
            print(f'Your current balance is {balance}')
else:
    print('You entered the wrong pin...Try Again')
