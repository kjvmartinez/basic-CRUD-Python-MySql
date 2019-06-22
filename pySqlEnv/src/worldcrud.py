import mysql.connector
from mysql.connector import errorcode

config = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'database' : 'world',
    'raise_on_warnings' : True
}
try:
    conn = mysql.connector.connect(**config)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    print("connected")
    conn.close()


def insert_city(val):
    conn = mysql.connector.connect(user='root')
    cursor = conn.cursor()
    query = "INSERT INTO world.city (name, countrycode, district, population) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, val)
    print(cursor.rowcount, "record inserted.")
    conn.commit()
    conn.close()

def update_city(val):
    conn = mysql.connector.connect(user="root")
    cursor = conn.cursor()
    query = "UPDATE world.city SET name = %s, countrycode = %s, district = %s, population = %s WHERE id = %s"
    cursor.execute(query, val)
    print(cursor.rowcount, "record updated.")
    conn.commit()
    conn.close()

def delete_city(val):
    conn = mysql.connector.connect(user="root")
    cursor = conn.cursor()
    query = "DELETE FROM world.city WHERE id =%s"
    cursor.execute(query, val)
    print(cursor.rowcount, "record deleted.")
    conn.commit()
    conn.close()

def view_city():
    conn = mysql.connector.connect(user="root")
    cursor = conn.cursor()
    query = "SELECT * FROM world.city limit 50"
    cursor.execute(query)
    rows = cursor.fetchall()
    for x in rows:
        print(x)
    conn.close()
    

'''
Inserting data to city table
'''
# city_data = ("Puerto Princesa", "PPC", "San Jose", 100)
# insert_city(city_data)


'''
Updating data from city table
'''
# city_data = ("Puerto Princesa", "PPC", "San Jose", 500, 4082)
# update_city(city_data)

'''
Deleting data from city table
'''
# city_data = (4079, )
# delete_city(city_data)

'''
Display table city
'''
view_city()
