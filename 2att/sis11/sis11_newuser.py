import psycopg2

hostname = 'localhost'
database = 'postgres'
username = 'postgres'
pwd = 'qwerty'
port_id = 5432

conn = None
cur = None

sql = 'select * from phone'

# in the block try we will write request to tables

try:
    # connect to exist database

    conn = psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = pwd,
                port = port_id)
    cur = conn.cursor()
    
    # the cursor for perfoming database operations
    
    # create a new table
    cur.execute('DROP TABLE IF EXISTS phone')

    create_script = '''CREATE TABLE IF NOT EXISTS phone(
                              id      int
                              name    varchar(40) NOT NULL,
                              number  int)'''
    cur.execute(create_script)
        

        
    # insert data into a table
    insert_script = '''INSERT INTO phone (id, name, number) VALUES(%s, %s, %s)''' #2 %s folders for 2 column
    insert_values = [(1,'James', 880055) , (2,'Rob', 87764), (3,'Mary', 756)]
    for record in insert_values:
        cur.execute(insert_script, record)

    print("Record by pattern")
    variant = input()
    if variant == "y":
        pattern = input("Enter pattern... ")
        search = input("Search in... ")
        '''if search == "name":
            search_sql = f"select (user_id, username, numbers) from phone where \"username\" like '%{pattern}%';"
            cur.execute(search_sql)
        if search == "number":
            number = input("Enter number...")
            search_sql = f"select (user_id, username, numbers) from phone where where \"numbers\" like '%{pattern}%';"'''
            
        search_sql = f"select * from phone where \"{search}\" like '%{pattern}%';"
        cur.execute(search_sql)
        str_search = cur.fetchall()
        print(str_search)
    

    print("Do you want add new user")
    variant = input()
    if variant  == "y":
        id = input("Enter id... ")
        name = input("Enter name... ")
        number = input("Enter phone number...")
        cur.execute(f"select * from from phonebook where \"username\" like '%{pattern}%';")
        print(len(cur.fetchall()))
        if len(cur.fetchall()) > 0 :
            cur.execute(f"update phonebook set \"username\" = '{name}' where \"user_id\" = '{id}';")
            cur.execute(f"update phonebook set \"numbers\" = '{name}' where \"user_id\" = '{id}';")
        else:
            cur.execute(f"insert into phonebook (user_id, username, numbers) values ({id}, '{name}', {number});")
    
    
except Exception as error:
    print(error)

finally:
    if conn is not None:
        conn.close()
    if cur is not None:
        cur.close()
