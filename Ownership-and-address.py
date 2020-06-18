import smartpy as sp

class Cryptobot(sp.Contract):
    # Pass manager_address as a parameter to the initialization function
   
    def __init__(self, life_state, manager_address):
        self.init(
            # Add bot_manager variable below
            bot_manager = manager_address,
            
            name = "terminator",
            is_alive = life_state,
            
            coordinate_x = sp.int(0), 
            coordinate_y = sp.nat(0), 
            
            plasma_bullet_count = 5,
            
            record_alien_kills = {
                "simple_alien": sp.nat(0),
                "boss_alien": sp.nat(0)
            }
        )
        
    @sp.entry_point
    def change_name(self, new_name):
        self.data.name = new_name
             
    @sp.entry_point
    def move_horizontally(self, update_to):
        self.data.coordinate_x += update_to
    
    @sp.entry_point
    def move_vertically(self, update_to):
        self.data.coordinate_y += update_to

    @sp.entry_point
    def shoot_alien(self, alien_type): 
        self.data.plasma_bullet_count -= 1
        self.data.record_alien_kills[alien_type] += 1
     
@sp.add_test(name = "Simulating ownership")
def test():
    scenario = sp.test_scenario()
   
    # Define my_address variable below
    # and give it the address value of tz1Syu3KacZ8cy4286a4vaCeoMtwqVKHkaoj
    my_address = sp.address("tz1Syu3KacZ8cy4286a4vaCeoMtwqVKHkaoj")
    # Pass my_address as value to manager_address
    # and then use it to invoke the class
    test_bot =  Cryptobot(life_state = True, manager_address= my_address)
   
    scenario += test_bot
          
    scenario += test_bot.shoot_alien("simple_alien")
   
    scenario += test_bot.shoot_alien("boss_alien")
