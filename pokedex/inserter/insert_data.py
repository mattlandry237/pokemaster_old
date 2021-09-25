import csv
import psycopg2



if __name__ == '__main__':
    insert_types = False
    insert_names = False
    insert_poketypes = False
    insert_type_eff = True

    dsn = {
        'user': 'postgres',
        'dbname': 'postgres',
        'host': 'localhost',
        'password': 'postgres'
    }

    db_conn = psycopg2.connect(**dsn)
    cur = db_conn.cursor()
    if insert_types:
        with open('pokemon_types.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader) # Skips the header row
            for row in reader:
                cur.execute(
                    "INSERT INTO type_chart (type_name) VALUES (%s)", row
                )
    
    if insert_names:
        with open('pokenames.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                cur.execute(
                    "INSERT INTO pokemon (dex_num, poke_name) VALUES (%s, %s)", row
                )
    
    if insert_poketypes:
        with open('poketypes_1.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                print(row)
                cur.execute(
                    "INSERT INTO assn_poke_type (poke_id, type_id) VALUES (%s, %s)", row
                )
        
        with open('poketypes_2.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                print(row)
                cur.execute(
                    "INSERT INTO assn_poke_type (poke_id, type_id) VALUES (%s, %s)", row
                )

    if insert_type_eff:
        with open('poke_type_eff.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                print(row)
                cur.execute(
                    "INSERT INTO assn_type_eff (atk_type_id, def_type_id, eff_rate) VALUES (%s, %s, %s)", row
                )


    
    cur.close()
    db_conn.commit()
    db_conn.close()



