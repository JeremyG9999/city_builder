import matplotlib.pyplot as plt
import sqlite3

DB_FILE = 'database_layer/citybuilder.db'

def fetch_latest_game_state():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('SELECT food, wood, wealth, metal, knowledge FROM game_state')
    row = c.fetchone()
    conn.close()
    if row is None:
        return 0, 0, 0, 0, 0
    else:
        return row

def generate_resource_chart():
    food, wood, wealth, metal, knowledge = fetch_latest_game_state()

    plt.bar('Food', food)
    plt.bar('Wood', wood)
    plt.bar('Wealth', wealth)
    plt.bar('Metal', metal)
    plt.bar('Knowledge', knowledge)

    plt.xlabel('Resource')
    plt.ylabel('Amount')
    plt.title('Current Game Resources')
    plt.grid(True)
    plt.show()