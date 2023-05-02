import psycopg2 

hostname = 'localhost'
database = 'postgres'
username = 'postgres'
pwd = 'qwerty'
port_id = 5432

conn = None
cur = None

#sql1 = 'select* from phonebook'

variant = input()


try:
    conn = psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = pwd,
                port = port_id)
    cur = conn.cursor()

    if variant == "csv":
        f = open('phone.csv', 'r')
        cur.copy_from(f, 'phonebook', sep =';')
        f.close()
    if variant == "change":
        change = input("What do you want to change?")
        if change == "name":
            name = input('Name to set...')
            condition = input('Where do you want to set changes ')
            update_sql = f"update phone set \"name\" = '{name}' where \"number\" = '{condition}';"
        if change == "number":
            num = input('Phone number to set...')
            condition = input('Where do you want to set changes ')
            update_sql = f"update phone set \"number\" = '{num}' where \"name\" = '{condition}';"
        cur.execute(update_sql)
    conn.commit()  
    #print("Record inserted successfully")  
    cur.execute()



    number = cur.fetchall()
    conn.commit()

except Exception as error:
        print(error)
    
finally:
        if conn is not None:
                cur.close()
        if cur is not None:
                conn.close()
        



