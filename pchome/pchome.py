import requests
import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'pchome'

try:
    cnx = mysql.connector.connect(user='root',
                                  password='sleeps09',
                                  host='127.0.0.1',
                                  auth_plugin='mysql_native_password')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    print('成功連線MySQL Server')

cursor = cnx.cursor()


def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(DB_NAME))
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)

# creating table
TABLES = {}
TABLES['product'] = (
    "CREATE TABLE `product` ("
    "  `name` varchar(50) NOT NULL,"
    "  `price` int NOT NULL,"
    "  PRIMARY KEY (`name`)"
    ") ENGINE=InnoDB")

for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

add_product = ("INSERT IGNORE INTO product "
               "(name, price) "
               "VALUES (%s, %s)")

for i in range(1, 4):
    url = f'https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=%E6%9B%B2%E9%9D%A2%E8%9E%A2%E5%B9%95%2024%E5%90%8B&page={i}&sort=sale/dc'
    re = requests.get(url)
    if re.status_code != requests.codes.ok:
        print(i, 'error', re.status_code)
        continue

    data = re.json()
    # pprint.pprint(data)
    # print(data['prods'][0]['name'])
    # print(data['prods'][0]['price'])
    for product in data['prods']:
        name = product['name']
        price = product['price']
        if len(name) > 50:
            name = name[:50]
        print(name)
        print(price)
        data_product = (name, price)
        # Insert new product
        cursor.execute(add_product, data_product)

# Make sure data is committed to the database
cnx.commit()

print('關閉中')
cursor.close()
cnx.close()
