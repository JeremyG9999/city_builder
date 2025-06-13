import time
import colorama
import sys
import os
import shutil
from game_scripts.menu import PauseMenu
from game_scripts.production import Production
colorama.init()

class CityBuilderGame:
    def __init__(self):
        sys.stdout.write('\033[?25l')
        self.food = 100
        self.wood = 100
        self.metal = 0
        self.wealth = 0
        self.knowledge = 0
        self.time_counter = 0
        self.farmer = 1
        self.woodcutter = 1
        self.merchant = 0
        self.miner = 0
        self.scholar = 0
        self.citizen_population = 2
        self.total_population = 2
        self.population_limit = 25
        self.age_number = 1 
        self.military_research = 0
        self.civics_research = 0
        self.commerce_research = 0 
        self.science_research = 0 
        self.paused = False   
        self.running = True  
        self.pause_menu = PauseMenu(self) # an attribute that holds a reference to an object pointing to PauseMenu instance
        self.production = Production(self)
        self.last_time = time.time()
        self.last_terminal_size = shutil.get_terminal_size()

    def age_name(self):
        if self.age_number == 1:
            age = "Villager Phase"
        elif self.age_number == 2:
            age = "City-State Stage"
        elif self.age_number == 3:
            age = "Regional-Hegemony Era"
        elif self.age_number == 4:
            age = "Nation-State Period"
        elif self.age_number == 5:
            age = "Empire Age"
        return age

    def game_play(self):
        if not self.paused:
            print("\033[H\033[3J", end='', flush=True)
            print("+" + "-"*113 + "+", flush=True)
            print("|" + ("The " + self.age_name()).center(113) + "|", flush=True)
            print("+" + "-"*16 + "+" + "-"*96 + "+", flush=True)
            print("| Category       | Details | (Use capital letters to buy/sell 5 units)" + " " * 44 + "|", flush=True)
            print("+" + "-"*16 + "+" + "-"*96 + "+", flush=True)
            print(f"| Resources      | f-Food-q: {self.food:<6} | t-Wood-e: {self.wood:<6} | w-Wealth: {self.wealth:<6} | m-Metal: {self.metal:<6} | k-Knowledge: {self.knowledge:<6} |", flush=True)
            print("+" + "-"*16 + "+" + "-"*96 + "+", flush=True)
            print(f"| Citizens       | Farmer: {self.farmer} -50f | Wood Cutter: {self.woodcutter} -50f | Merchant: {self.merchant} -500FT | Scholar: {self.scholar} -350W | Miner: {self.miner} -400W |", flush=True)
            print("+" + "-"*16 + "+" + "-"*96 + "+", flush=True)
            print(f"| Population     | Citizens: {self.citizen_population:<6} | Total Pop: {self.total_population:<6} | Pop Limit: {self.population_limit:<6} |" + " "*37 + "|", flush=True)
            print("+" + "-"*16 + "+" + "-"*96 + "+", flush=True)
            print(f"| Research       | Age Level: {self.age_number:<7} | Military: {self.military_research:<7} | Civics: {self.civics_research:<7} | Commerce: {self.commerce_research:<7} | Science: {self.science_research:<6} |", flush=True)
            print("+" + "-"*16 + "+" + "-"*96 + "+", flush=True)
            print(f"| Pause Options  | P-Pause | S-Save | L-Load | Q-Quit | " + " "*58 + "|", flush=True)
            print("+" + "-"*16 + "+" + "-"*96 + "+", flush=True)

            print("\n| Library     | (type '1' to advance age, '2' is military, '3' is civics, '4' is commerce, '5' is science)", flush=True)
            print("+" + "-"*114 + "+", flush=True)
            print("| Category    | Level 1           | Level 2           | Level 3            | Level 4           | Level 5           |", flush=True)
            print("+" + "-"*114 + "+", flush=True)
            print("| Age Level   |       N/A         |       500FT       | 1.5k-FT 500W 250K  | 6k-FT 2k-W 1k-MK  | 12k-FT 5k-W 3k-MK |", flush=True)
            print("+" + "-"*114 + "+", flush=True)
            print("| Military    |       250FT       | 500FT 200W 100K   | 1k-FT 500W 250MK   | 2k-FT 1k-W 500MK  | 4k-FT 2k-W 1k-MK  |", flush=True)
            print("+" + "-"*114 + "+", flush=True)
            print("| Civics      |       250FT       | 500FT 200W 100K   | 1k-FT 500W 250MK   | 2k-FT 1k-W 500MK  | 4k-FT 2k-W 1k-MK  |", flush=True)
            print("+" + "-"*114 + "+", flush=True)
            print("| Commerce    |       250FT       | 500FT 200W 100K   | 1k-FT 500W 250MK   | 2k-FT 1k-W 500MK  | 4k-FT 2k-W 1k-MK  |", flush=True)
            print("+" + "-"*114 + "+", flush=True)
            print("| Science     |       250FT       | 500FT 200W 100K   | 1k-FT 500W 250MK   | 2k-FT 1k-W 500MK  | 4k-FT 2k-W 1k-MK  |", flush=True)
            print("+" + "-"*114 + "+", flush=True)


            self.food += self.production.food_production()
            self.wood += self.production.wood_production()
            self.wealth += self.production.merchant_production()
            self.metal += self.production.metal_production()
            self.knowledge += self.production.knowledge_production()
            self.time_counter += 1

    def sizing(self):
        current_size = shutil.get_terminal_size()
        if current_size != self.last_terminal_size:
            self.last_terminal_size = current_size
            self.cls()
        
    def master_game_loop(self):
        while self.running:
            self.sizing()
            self.pause_menu.pause_menu_in_game()
            current_time = time.time()
            if current_time - self.last_time >= 1:
                self.last_time = current_time
                self.game_play()          

    def cls(self):
        os.system("cls" if os.name == "nt" else "clear")

def main():
    game = CityBuilderGame()
    game.master_game_loop()