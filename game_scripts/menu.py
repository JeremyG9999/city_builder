import os
import msvcrt
import sys
import time
from database_layer.db_file import load_game, save_game

class PauseMenu:
    def __init__(self, game):
        self.game = game  # attribute to hold PauseMenu reference

    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def get_key_press(self):
        if msvcrt.kbhit():
            return msvcrt.getch()
        return None
    
    def pause_menu_in_game(self):
        key = self.get_key_press()

        if key == b'p':
            self.game.paused = not self.game.paused
            if not self.game.paused:
                self.cls()
        elif key == b'r':
            pass
        elif key == b'l' and self.game.paused:
            self.load_saved_game()
            time.sleep(1)
            print("\nGame Loaded Successfully")
        elif key == b's' and self.game.paused:
            data = self.get_save_data()
            save_game(*data)
            time.sleep(1)
            print("\nGame Saved Successfully")
        elif key == b'q' and self.game.paused:
            sys.stdout.write('\033[?25h')
            self.game.running = False
            self.cls()
        elif key == b'1':
            self.age_research()
        elif key == b'2':
            self.military_research() 
        elif key == b'3':
            self.civics_research() 
        elif key == b'4':
            self.commerce_research() 
        elif key == b'5':
            self.science_research() 
        elif key == b'f':
            self.buy_farmer()
        elif key == b'F':
            self.buy_5_farmer()
        elif key == b'q':
            self.del_farmer()
        elif key == b'Q':
            self.del_5_farmer()
        elif key == b't':
            self.buy_woodcutter()
        elif key == b'e':
            self.del_woodcutter()
        elif key == b'w':
            self.buy_merchant()
        elif key == b'm':
            self.buy_miner()
        elif key == b'k':
            self.buy_scholar()
    
    def military_research(self):
        if self.game.food >= 250 and self.game.wood >= 250 and self.game.military_research == 0 and self.game.age_number == 1:
            self.game.food -= 250
            self.game.wood -= 250
            self.game.military_research += 1
        elif self.game.food >= 500 and self.game.wood >= 500 and self.game.wealth >= 200 and self.game.knowledge >= 100 and self.game.military_research == 1 and self.game.age_number == 2:
            self.game.food -= 500
            self.game.wood -= 500
            self.game.wealth -= 200
            self.game.knowledge -= 100
            self.game.military_research += 1
        elif self.game.food >= 1000 and self.game.wood >= 1000 and self.game.wealth >= 500 and self.game.knowledge >= 250 and self.game.metal and self.game.military_research == 2 and self.game.age_number == 3:
            self.game.food -= 1000
            self.game.wood -= 1000
            self.game.wealth -= 500
            self.game.knowledge -= 250
            self.game.metal -= 250
            self.game.military_research += 1
        elif self.game.food >= 2000 and self.game.wood >= 2000 and self.game.wealth >= 1000 and self.game.knowledge >= 500 and self.game.metal >= 500 and self.game.military_research == 3 and self.game.age_number == 4:
            self.game.food -= 2000
            self.game.wood -= 2000
            self.game.wealth -= 1000
            self.game.knowledge -= 500
            self.game.metal -= 500
            self.game.military_research += 1
        elif self.game.food >= 4000 and self.game.wood >= 4000 and self.game.wealth >= 2000 and self.game.knowledge >= 1000 and self.game.metal >= 1000 and self.game.military_research == 4 and self.game.age_number == 5:
            self.game.food -= 4000
            self.game.wood -= 4000
            self.game.wealth -= 2000
            self.game.knowledge -= 1000
            self.game.metal -= 1000
            self.game.military_research += 1

    def commerce_research(self):
        if self.game.food >= 250 and self.game.wood >= 250 and self.game.commerce_research == 0 and self.game.age_number == 1:
            self.game.food -= 250
            self.game.wood -= 250
            self.game.commerce_research += 1
        elif self.game.food >= 500 and self.game.wood >= 500 and self.game.wealth >= 200 and self.game.knowledge >= 100 and self.game.commerce_research == 1 and self.game.age_number == 2:
            self.game.food -= 500
            self.game.wood -= 500
            self.game.wealth -= 200
            self.game.knowledge -= 100
            self.game.commerce_research += 1
        elif self.game.food >= 1000 and self.game.wood >= 1000 and self.game.wealth >= 500 and self.game.knowledge >= 250 and self.game.metal >= 250 and self.game.commerce_research == 2 and self.game.age_number == 3:
            self.game.food -= 1000
            self.game.wood -= 1000
            self.game.wealth -= 500
            self.game.knowledge -= 250
            self.game.metal -= 250
            self.game.commerce_research += 1
        elif self.game.food >= 2000 and self.game.wood >= 2000 and self.game.wealth >= 1000 and self.game.knowledge >= 500 and self.game.metal >= 500 and self.game.commerce_research == 3 and self.game.age_number == 4:
            self.game.food -= 2000
            self.game.wood -= 2000
            self.game.wealth -= 1000
            self.game.knowledge -= 500
            self.game.metal -= 500
            self.game.commerce_research += 1
        elif self.game.food >= 4000 and self.game.wood >= 4000 and self.game.wealth >= 2000 and self.game.knowledge >= 1000 and self.game.metal >= 1000 and self.game.commerce_research == 4 and self.game.age_number == 5:
            self.game.food -= 4000
            self.game.wood -= 4000
            self.game.wealth -= 2000
            self.game.knowledge -= 1000
            self.game.metal -= 1000
            self.game.commerce_research += 1

    def science_research(self):
        if self.game.food >= 250 and self.game.wood >= 250 and self.game.science_research == 0 and self.game.age_number == 1:
            self.game.food -= 250
            self.game.wood -= 250
            self.game.science_research += 1
        elif self.game.food >= 500 and self.game.wood >= 500 and self.game.wealth >= 200 and self.game.knowledge >= 100 and self.game.science_research == 1 and self.game.age_number == 2:
            self.game.food -= 500
            self.game.wood -= 500
            self.game.wealth -= 200
            self.game.knowledge -= 100
            self.game.science_research += 1
        elif self.game.food >= 1000 and self.game.wood >= 1000 and self.game.wealth >= 500 and self.game.knowledge >= 250 and self.game.metal >= 250 and self.game.science_research == 2 and self.game.age_number == 3:
            self.game.food -= 1000
            self.game.wood -= 1000
            self.game.wealth -= 500
            self.game.knowledge -= 250
            self.game.metal -= 250
            self.game.science_research += 1
        elif self.game.food >= 2000 and self.game.wood >= 2000 and self.game.wealth >= 1000 and self.game.knowledge >= 500 and self.game.metal >= 500 and self.game.science_research == 3 and self.game.age_number == 4:
            self.game.food -= 2000
            self.game.wood -= 2000
            self.game.wealth -= 1000
            self.game.knowledge -= 500
            self.game.metal -= 500
            self.game.science_research += 1
        elif self.game.food >= 4000 and self.game.wood >= 4000 and self.game.wealth >= 2000 and self.game.knowledge >= 1000 and self.game.metal >= 1000 and self.game.science_research == 4 and self.game.age_number == 5:
            self.game.food -= 4000
            self.game.wood -= 4000
            self.game.wealth -= 2000
            self.game.knowledge -= 1000
            self.game.metal -= 1000
            self.game.science_research += 1

    def civics_research(self):
        if self.game.food >= 250 and self.game.wood >= 250 and self.game.civics_research == 0 and self.game.age_number == 1:
            self.game.food -= 250
            self.game.wood -= 250
            self.game.civics_research += 1
        elif self.game.food >= 500 and self.game.wood >= 500 and self.game.wealth >= 200 and self.game.knowledge >= 100 and self.game.civics_research == 1 and self.game.age_number == 2:
            self.game.food -= 500
            self.game.wood -= 500
            self.game.wealth -= 200
            self.game.knowledge -= 100
            self.game.civics_research += 1
        elif self.game.food >= 1000 and self.game.wood >= 1000 and self.game.wealth >= 500 and self.game.knowledge >= 250 and self.game.metal >= 250 and self.game.civics_research == 2 and self.game.age_number == 3:
            self.game.food -= 1000
            self.game.wood -= 1000
            self.game.wealth -= 500
            self.game.knowledge -= 250
            self.game.metal -= 250
            self.game.civics_research += 1
        elif self.game.food >= 2000 and self.game.wood >= 2000 and self.game.wealth >= 1000 and self.game.knowledge >= 500 and self.game.metal >= 500 and self.game.civics_research == 3 and self.game.age_number == 4:
            self.game.food -= 2000
            self.game.wood -= 2000
            self.game.wealth -= 1000
            self.game.knowledge -= 500
            self.game.metal -= 500
            self.game.civics_research += 1
        elif self.game.food >= 4000 and self.game.wood >= 4000 and self.game.wealth >= 2000 and self.game.knowledge >= 1000 and self.game.metal >= 1000 and self.game.civics_research == 4 and self.game.age_number == 5:
            self.game.food -= 4000
            self.game.wood -= 4000
            self.game.wealth -= 2000
            self.game.knowledge -= 1000
            self.game.metal -= 1000
            self.game.civics_research += 1

    def age_research(self): # 1 to 2
        if self.game.age_number == 1 and self.game.food >= 500 and self.game.wood >= 500 and self.game.military_research == 1 and self.game.civics_research == 1 and self.game.commerce_research == 1 and self.game.science_research == 1: 
            self.game.food -= 500
            self.game.wood -= 500
            self.game.age_number += 1
            self.game.population_limit += 25
        elif self.game.age_number == 2 and self.game.food >= 1500 and self.game.wood >= 1500 and self.game.wealth >= 500 and self.game.knowledge >= 250 and self.game.military_research == 2 and self.game.civics_research == 2 and self.game.commerce_research == 2 and self.game.science_research == 2: 
            self.game.food -= 1500 
            self.game.wood -= 1500
            self.game.wealth -= 500
            self.game.knowledge -= 250
            self.game.age_number += 1
            self.game.population_limit += 25
        elif self.game.age_number == 3 and self.game.food >= 6000 and self.game.wood >= 6000 and self.game.wealth >= 2000 and self.game.metal >= 1000 and self.game.knowledge >= 1000 and self.game.military_research == 3 and self.game.civics_research == 3 and self.game.commerce_research == 3 and self.game.science_research == 3: 
            self.game.food -= 6000
            self.game.wood -= 6000
            self.game.wealth -= 2000
            self.game.metal -= 1000
            self.game.knowledge -= 1000
            self.game.age_number += 1
            self.game.population_limit += 25
        elif self.game.age_number == 4 and self.game.food >= 12000 and self.game.wood >= 12000 and self.game.wealth >= 5000 and self.game.metal >= 3000 and self.game.knowledge >= 3000 and self.game.military_research == 4 and self.game.civics_research == 4 and self.game.commerce_research == 4 and self.game.science_research == 4: 
            self.game.food -= 12000
            self.game.wood -= 12000
            self.game.wealth -= 5000
            self.game.metal -= 3000
            self.game.knowledge -= 3000
            self.game.age_number += 1
            self.game.population_limit += 25

    def buy_farmer(self):
        if self.game.food >= 50 and self.game.population_limit > self.game.total_population:
            self.game.food -= 50
            self.game.farmer += 1
            self.game.total_population += 1
            self.game.citizen_population += 1
        else:
            return None
        
    def buy_5_farmer(self): # make more later on
        if self.game.food >= 250 and self.game.population_limit >= self.game.total_population + 5:
            self.game.food -= 250
            self.game.farmer += 5
            self.game.total_population += 5
            self.game.citizen_population += 5
        else:
            return None
    
    def del_farmer(self): # make more del later on
        if self.game.farmer >= 2:
            self.game.farmer -= 1
            self.game.citizen_population -= 1
            self.game.total_population -= 1

    def del_5_farmer(self): # make more del later on
        if self.game.farmer >= 6:
            self.game.farmer -= 5
            self.game.citizen_population -= 5
            self.game.total_population -= 5
    
    def buy_woodcutter(self):
        if self.game.food >= 50 and self.game.population_limit > self.game.total_population:
            self.game.food -= 50
            self.game.woodcutter += 1
            self.game.total_population += 1
            self.game.citizen_population += 1
        else:
            return None
        
    def del_woodcutter(self): 
        if self.game.woodcutter >= 2:
            self.game.woodcutter -= 1
            self.game.citizen_population -= 1
            self.game.total_population -= 1
        
    def buy_merchant(self):
        if self.game.food >= 500 and self.game.wood >= 500 and self.game.population_limit > self.game.total_population and self.game.age_number >= 2:
            self.game.food -= 500
            self.game.wood -= 500
            self.game.merchant += 1
            self.game.total_population += 1
            self.game.citizen_population += 1
        else:
            return None
        
    def buy_scholar(self):
        if self.game.wealth >= 350 and self.game.population_limit > self.game.total_population and self.game.age_number >= 2:
            self.game.wealth -= 350
            self.game.scholar += 1
            self.game.total_population += 1
            self.game.citizen_population += 1
        else:
            return None
        
    def buy_miner(self):
        if self.game.wealth >= 400 and self.game.population_limit > self.game.total_population and self.game.age_number >= 3:
            self.game.wealth -= 400
            self.game.miner += 1
            self.game.total_population += 1
            self.game.citizen_population += 1
        else:
            return None

    def load_saved_game(self):
        data = load_game()
        if data is None:
            pass
        else:
            (
                self.game.food,
                self.game.wood,
                self.game.wealth,
                self.game.metal,
                self.game.knowledge,
                self.game.time_counter,
                self.game.farmer,
                self.game.woodcutter,
                self.game.merchant,
                self.game.miner,
                self.game.scholar,
                self.game.citizen_population,
                self.game.soldier_population,
                self.game.total_population,
                self.game.population_limit,
                self.game.city_count,
                self.game.age_number,
                self.game.military_research,
                self.game.civics_research,
                self.game.commerce_research,
                self.game.science_research
            ) = data
    def get_save_data(self):
        return (
            self.game.food,
            self.game.wood,
            self.game.wealth,
            self.game.metal,
            self.game.knowledge,
            self.game.time_counter,
            self.game.farmer,
            self.game.woodcutter,
            self.game.merchant,
            self.game.miner,
            self.game.scholar,
            self.game.citizen_population,
            self.game.soldier_population,
            self.game.total_population,
            self.game.population_limit,
            self.game.city_count,
            self.game.age_number,
            self.game.military_research,
            self.game.civics_research,
            self.game.commerce_research,
            self.game.science_research
        )