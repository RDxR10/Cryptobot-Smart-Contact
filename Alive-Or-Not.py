import smartpy as sp

class Cryptobot(sp.Contract):
    #2. Add life_state as a parameter to the the __init__ function:
    def __init__(self, life_state):
        self.init(
            name = "terminator",
            #1. add is_alive state variable beneath
            is_alive = life_state
            #3.^Give is_alive the value of life_state
        )
        
    @sp.entry_point
    def change_name(self, new_name):
        self.data.name = new_name
        
@sp.add_test(name = "Test whether Cryptobot is alive or not")
def test():
    scenario = sp.test_scenario()
    
    #4. Pass life_state = True to Cryptobot’s class invocation:
    test_bot =  Cryptobot(life_state = True)
    
    scenario += test_bot
            
    #5. Test for whether the Cryptobot is alive or not beneath: 
    scenario.verify(test_bot.data.is_alive == True)
