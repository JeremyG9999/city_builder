import os

from game_scripts.city_builder import CityBuilderGame
from game_scripts.chart import generate_resource_chart
from database_layer.db_file import setup_db, load_game, delete_saved_game

class Menu:
    def main_menu(self):
        self.cls()
        setup_db()
        while True:
            print("\n=== CITY BUILDER ===")
            print("1. Start New Game (Press p to pause)")
            print("2. Load Last Saved Data")
            print("3. Delete Saved Data")
            print("4. View Saved Data Chart")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.cls()
                CityBuilderGame().master_game_loop()
            elif choice == "2":
                self.load_and_start_game()
            elif choice == "3":
                delete_saved_game()
                self.cls()
                print("Saved data deleted.")
            elif choice == "4":
                self.cls()
                generate_resource_chart()
            elif choice == "5":
                self.cls()
                break
            else:
                self.cls()
                print("Invalid choice. Please enter a number from 1 to 5.")

    def load_and_start_game(self):
        data = load_game()
        if data is None:
            self.cls()
            print("No saved game found.")
        else:
            self.cls()
            game = CityBuilderGame()
            (
                game.food,
                game.wood,
                game.metal,
                game.wealth,
                game.knowledge,
                game.time_counter,
                game.farmer,
                game.woodcutter,
                game.merchant,
                game.miner,
                game.scholar,
                game.citizen_population,
                game.total_population,
                game.population_limit,
                game.age_number,
                game.military_research,
                game.civics_research,
                game.commerce_research,
                game.science_research
            ) = data
            game.master_game_loop()

    def cls(self):
        os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    Menu().main_menu()