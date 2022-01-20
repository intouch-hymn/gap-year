#Seperate banknotes Program

print("---Wecome to Seperate banknotes Program ---\n")

number = int(input('Please insert your money'))

if number >= 1000 :
    print('1000thb =',number//1000,'pieces')
    number %= 1000

if number >= 500 :
    print('500thb =',number//500,'pieces')
    number %= 500

if number >= 100 :
    print('100thb =',number//100,'pieces')
    number %= 100
