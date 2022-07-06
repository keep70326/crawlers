import datetime
import mysql.connector

cnx = mysql.connector.connect(user='root', password='sleeps09', host='127.0.0.1', database='pchome')


cursor = cnx.cursor(dictionary=True)

query = ("SELECT * FROM product "
         "WHERE price > 5000") #"WHERE name LIKE '%ASUS%'"

# hire_start = datetime.date(1999, 1, 1)
# hire_end = datetime.date(1999, 12, 31)

cursor.execute(query)

# for (first_name, last_name, hire_date) in cursor:
#   print("{}, {} was hired on {:%d %b %Y}".format(
#     last_name, first_name, hire_date))
for row in cursor:
    # print(row)
    print(row['name'])

cursor.close()
cnx.close()