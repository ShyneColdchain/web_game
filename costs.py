# wallet module  
def start_money():
    money = 30
    return money

def double(money):
    money += 5
    return money
    
def triple(money):
    money += 20
    return money
    
def turn_cost(money):
    money -= 2
    return money
    
def casino_cost(money):
    money -= 3
    return money
    
def train_cost(money):
    money -= 5
    return money
    
def prompt_money(money):
    if money <= 0:
        print "You are out of money!"
        return False
    else:
        print "\nYou have $%i left in your wallet." % money
        return True