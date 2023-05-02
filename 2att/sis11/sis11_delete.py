import psycopg2

hostname = 'localhost'
database = 'postgres'
username = 'postgres'
pwd = 'qwerty'
port_id = 5432

conn = None
cur = None

sql = 'select * from phonebook'

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
    cur.execute('DROP TABLE IF EXISTS phonebook')

    create_script = '''CREATE TABLE IF NOT EXISTS phonebook(
                              name    varchar(40) NOT NULL,
                              number  int)'''
    cur.execute(create_script)
        

        
    # insert data into a table
    insert_script = '''INSERT INTO phonebook (name, number) VALUES( %s, %s)''' #2 %s folders for 2 column
    insert_values = [('James', 880055) , ('Rob', 87764), ('Mary', 756)]
    for record in insert_values:
        cur.execute(insert_script, record)



    print("Delete by pattern?")
    variant = input()
    if variant == "y":
        pattern = input("Enter pattern... ")
        search = input("Search in... ")
        '''if search == "name":
            search_sql = f"select (user_id, username, numbers) from phonebook where \"username\" like '%{pattern}%';"
            cur.execute(search_sql)
        if search == "number":
            number = input("Enter number...")
            search_sql = f"select (user_id, username, numbers) from phonebook where where \"numbers\" like '%{pattern}%';"'''
            
        search_sql = f"select * from phonebook where \"{search}\" like '%{pattern}%';"
        cur.execute(search_sql)
        str_search = cur.fetchall()
        print(str_search)
    
    
    
    print("Delete by pattern?")
    var1 = input()

    if var1 == "y":
        pattern = input("By what delete...")
        condition = input("Data to delete ")
        delete_sql = f"delete from phonebook where  \"{condition}\" like '%{pattern}%'"
        cur.execute(delete_sql)
        cur.execute(sql)
        conn.commit()

 
    
except Exception as error:
    print(error)

finally:
    if conn is not None:
        conn.close()
    if cur is not None:
        cur.close()

