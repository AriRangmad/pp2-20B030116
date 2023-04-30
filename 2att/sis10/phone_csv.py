import psycopg2 

conn = psycopg2.connect(
host = "localhost",
database = "postgre",
user = "postgres",
password = "qwerty")


sql1 = 'select* from phone'
cur = conn.cursor()
variant = input()



if variant == "csv":
    f = open('phone.csv', 'r')
    cur.copy_from(f, 'phone', sep =';')
    f.close()
if variant == "change":
    change = input("What do you want to change?")
    if change == "name":
        name = input('Name to set...')
        condition = input('Where do you want to set changes ')
        update_sql = f"update phone set \"username\" = '{name}' where \"numbers\" = '{condition}';"
    if change == "number":
        num = input('Phone number to set...')
        condition = input('Where do you want to set changes ')
        update_sql = f"update phone set \"numbers\" = '{num}' where \"username\" = '{condition}';"
    cur.execute(update_sql)
conn.commit()  
print("Record inserted successfully")  
cur.execute(sql1)



numbers = cur.fetchall()
conn.commit()
print(numbers)
conn.close()