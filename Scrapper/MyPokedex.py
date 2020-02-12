import sqlite3

def addToBdd(id, name, type):

    conn = sqlite3.connect('my_pokedex.db')

    c = conn.cursor()

    # Create table
    c.execute('''CREATE TABLE IF NOT EXISTS pokedex(
            id INTEGER NOT NULL UNIQUE , 
            name TEXT NOT NULL UNIQUE,
            type TEXT NOT NULL
            )''')

    # Insert the row passed in argument
    pokemon = (id, name, type)
    if(getPokemon(id)==None):
        c.execute("INSERT INTO pokedex VALUES (?, ?, ?)", pokemon)

    # Save changes
    conn.commit()

    # close de bdd connection
    conn.close()

def getPokemon(id):

    conn = sqlite3.connect('my_pokedex.db')

    c = conn.cursor()

    # Return one pokemon with specification id
    c.execute("SELECT * FROM pokedex WHERE id = '%i'" %id)
    return(c.fetchone())

def getAll():

    conn = sqlite3.connect('my_pokedex.db')

    c = conn.cursor()

    # Return all pokemon in the bdd
    c.execute("SELECT * FROM pokedex")
    return (c.fetchall())