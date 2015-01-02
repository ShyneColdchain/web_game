# wallet module  
def start_money():
    money = 30
    return money
    
def double(money):
    money += 5
    
def triple(money):
    money += 20
    
def turn_cost(money):
    money -= 2
    
def casino_cost(money):
    money -= 3
    
def train_cost(money):
    money -= 5
    
def prompt_money(money):
    if money <= 0:
        print "You are out of money!"
        return False
    else:
        print "\nYou have $%i left in your wallet." % money
        return True