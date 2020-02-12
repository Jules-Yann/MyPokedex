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

    # Insert a row of data
    pokemon = (id, name, type)
    if(getPokemon(id)==None):
        c.execute("INSERT INTO pokedex VALUES (?, ?, ?)", pokemon)

    # Save the changes
    conn.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
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