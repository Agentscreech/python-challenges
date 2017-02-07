balance = 0

def deposit(num):
    global balance
    balance += num
    return balance

def withdraw(num):
    global balance
    balance -= num
    return balance

def check_balance(bal):
    return bal

def done():
    action = input("Are you done?\n")
    if action == "yes":
        print('Thank you!')
    elif action == "no":
        user_action()
    else:
        print("¯\\_(ツ)_/¯")
        print("I don't know what that means")
        done()

def user_action():
    command = input('What would you like to do? (deposit, withdraw, check_balance)\n')
    if command == "deposit":
        dep = input('How much would you like deposit? \n')
        deposit(int(dep))
        print('Your current balance is')
        print(check_balance(balance))
        done()
    elif command == "withdraw":
        wd = input('How much would you like to withdraw? \n')
        withdraw(int(wd))
        print('Your current balance is')
        print(check_balance(balance))
        done()
    elif command == "check_balance":
        print(check_balance(balance))
        done()
    else:
        print("¯\\_(ツ)_/¯")
        print("I don't know what that means")
        user_action()



print("Welcome to Chase bank.")

print("Your current balance is \n")
print(balance)
user_action()
