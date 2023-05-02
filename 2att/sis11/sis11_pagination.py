import psycopg2

hostname = 'localhost'
database = 'postgres'
username = 'postgres'
pwd = 'qwerty'
port_id = 5432

sql = '''SELECT * FROM phonebook'''



try:
        conn = psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = pwd,
                port = port_id)
        cur = conn.cursor()

        print("offset?")
        var=input()
        if var=="yes":
            print("Enter offset:")
            offset=int(input())
            sql+=" OFFSET {}".format(offset)
        print("limit?")


        var1=input()
        if var1=="yes":
            print("Enter limit:")
            limit=int(input())
            sql+=" LIMIT {}".format(limit)
        sql +=";"
        cur.execute(sql)
        #print(cur.fetchall())

    
        conn.commit()
        #cur.close()
        #conn.close() не лучший способ оставить это тут, тк при неожиданных ситуациях они просто закроются
        



except Exception as error:
        print(error)

finally:
        if conn is not None:
                cur.close()
        if cur is not None:
                conn.close()
        

