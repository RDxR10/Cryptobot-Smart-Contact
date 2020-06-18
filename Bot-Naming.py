import smartpy as sp

class Cryptobot(sp.Contract):
    def __init__(self):
        self.init(name = "terminator")

    # Add change_name entry function below
    @sp.entry_point
    def change_name(self, new_name):
        self.data.name = new_name

@sp.add_test(name = "Testing giving Cryptobot a new name")
def test():
    scenario = sp.test_scenario()
   
    test_bot =  Cryptobot()
   
    scenario += test_bot
   
    # Test change_name function below
    scenario += test_bot.change_name("punky terminator")
