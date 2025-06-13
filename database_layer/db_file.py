import sqlite3

DB_FILE = 'database_layer/citybuilder.db'

def setup_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS game_state (
            id INTEGER PRIMARY KEY,
            food INTEGER NOT NULL,
            wood INTEGER NOT NULL,
            wealth INTEGER NOT NULL,
            metal INTEGER NOT NULL,
            knowledge INTEGER NOT NULL,
            time_counter INTEGER NOT NULL,
            farmer INTEGER NOT NULL,
            woodcutter INTEGER NOT NULL,
            merchant INTEGER NOT NULL,
            miner INTEGER NOT NULL,
            scholar INTEGER NOT NULL,
            citizen_population INTEGER NOT NULL,
            total_population INTEGER NOT NULL,
            population_limit INTEGER NOT NULL,
            age_number INTEGER NOT NULL,
            military_research INTEGER NOT NULL,
            civics_research INTEGER NOT NULL,
            commerce_research INTEGER NOT NULL,
            science_research INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def save_game(
    food, wood, wealth, metal, knowledge, time_counter,
    farmer, woodcutter, merchant, miner, scholar,
    citizen_population, total_population,
    population_limit,age_number, military_research, 
    civics_research, commerce_research, science_research
):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('SELECT COUNT(*) FROM game_state')
    if c.fetchone()[0] == 0:
        c.execute('''
            INSERT INTO game_state (
                food, wood, wealth, metal, knowledge, time_counter,
                farmer, woodcutter, merchant, miner, scholar,
                citizen_population, total_population,
                population_limit, age_number, military_research, 
                civics_research, commerce_research, science_research
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            food, wood, wealth, metal, knowledge, time_counter,
            farmer, woodcutter, merchant, miner, scholar,
            citizen_population, total_population,
            population_limit, age_number, military_research, 
            civics_research, commerce_research, science_research
        ))
    else:
        c.execute('''
            UPDATE game_state SET
                food = ?, wood = ?, wealth = ?, metal = ?, knowledge = ?, time_counter = ?,
                farmer = ?, woodcutter = ?, merchant = ?, miner = ?, scholar = ?,
                citizen_population = ?, total_population = ?,
                population_limit = ?, age_number = ?, military_research = ?, 
                civics_research = ?, commerce_research = ?, science_research = ?
        ''', (
            food, wood, wealth, metal, knowledge, time_counter,
            farmer, woodcutter, merchant, miner, scholar,
            citizen_population, total_population,
            population_limit, age_number, military_research, 
            civics_research, commerce_research, science_research
        ))
    conn.commit()
    conn.close()

def load_game():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        SELECT
            food, wood, wealth, metal, knowledge, time_counter,
            farmer, woodcutter, merchant, miner, scholar,
            citizen_population, total_population,
            population_limit, age_number, military_research, 
            civics_research, commerce_research, science_research
        FROM game_state LIMIT 1
    ''')
    row = c.fetchone()
    conn.close()
    if row:
        return row
    else:
        return None

def delete_saved_game():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('DELETE FROM game_state')
    conn.commit()
    conn.close()