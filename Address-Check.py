import smartpy as sp

class Cryptobot(sp.Contract):
    def __init__(self, manager_address):
        self.init(
            bot_manager = manager_address,

            plasma_bullet_count = 5,

            record_alien_kills = {
                "simple_alien": sp.nat(0), 
                "boss_alien": sp.nat(0), 
            }
        )


    @sp.entry_point
    def shoot_alien(self, alien_type):
        sp.verify(
            self.data.bot_manager == sp.sender, 
            message = "Error: non manager call"
        )
        # Using sp.if add a condition to check plasma_bullet_count >= 1
        sp.if self.data.plasma_bullet_count >= 1:
            
            self.data.plasma_bullet_count -= 1
            self.data.record_alien_kills[alien_type] += 1
        # Use sp.else to run code when the above condition fails. 
        # Use sp.failwith to return an error message. 
        sp.else:
            sp.failwith("Error: you ran out of bullets! Please buy more!")

@sp.add_test(name = "Testing with sp if")
def test():
    scenario = sp.test_scenario()
    
    my_address = sp.address("tz1Syu3KacZ8cy4286a4vaCeoMtwqVKHkaoj")
    
    test_bot =  Cryptobot(manager_address = my_address)
    
    scenario += test_bot
    
    scenario += test_bot.shoot_alien("simple_alien").run(sender = my_address)
    scenario += test_bot.shoot_alien("boss_alien").run(sender = my_address)
