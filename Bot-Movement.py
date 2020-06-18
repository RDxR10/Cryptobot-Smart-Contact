import smartpy as sp

class Cryptobot(sp.Contract):
    def __init__(self, is_alive):
        self.init(
            name = "terminator",
            is_alive = is_alive,

            ## Add coordinate_x and coordinate_y variables
            ## Init both with 0 using sp.int and sp.nat respectively 
            coordinate_x=sp.int(0),
            coordinate_y=sp.nat(0)
        )
        
    @sp.entry_point
    def change_name(self, new_name):
        self.data.name = new_name

    # Define move_horizontally entry point function
    @sp.entry_point
    def move_horizontally(self, update_to):
        self.data.coordinate_x += update_to
        
        
    # Define move_vertically entry point function
    def move_vertically(self, update_to):
        self.data.coordinate_y += update_to
@sp.add_test(name = "Test Cryptobot movement")
def test():
    scenario = sp.test_scenario()
    
    test_bot =  Cryptobot(is_alive = True)
    
    scenario += test_bot
            
    # Test your movement entry functions below
    # Move Cryptobot forward by 2 and vertically by 1
    scenario += test_bot.move_horizontally(2)
    scenario += test_bot.move_vertically(1)
