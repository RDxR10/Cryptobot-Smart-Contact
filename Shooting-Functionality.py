import smartpy as sp

class Cryptobot(sp.Contract):
    def __init__(self, life_state):
        self.init(
            name = "terminator",
            is_alive = life_state,
            coordinate_x = sp.int(0), 
            coordinate_y = sp.nat(0), 
            
            # Add plasma_bullet_count with 5 bullets:
            plasma_bullet_count=5,
            
            # Add record_alien_kills below:
            self.init(
            record_alien_kills = {
                "simple_alien":sp.nat(0),
                "boss_alien":sp.nat(0)
            }
            )

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

            
    # Add shoot_alien function below
    @sp.entry_point
    def shoot_alien(self, alien_type): 
        # Reduce plasma_bullet_count by 1
        self.data.plasma_bullet_count-=1
            
        # Record the alien that was shot
        # and then increase it by 1 below
        self.data.record_alien_kills[alien_type] +=1
        
@sp.add_test(name = "Test shooting")
def test():
    scenario = sp.test_scenario()
    
    test_bot =  Cryptobot(life_state = True)
    
    scenario += test_bot

    # Use shoot_alien to kill 1 simple aliens and 1 boss alien
    scenario += test_bot.shoot_alien("simple_alien")
    scenario += test_bot.shoot_alien("boss_alien")
