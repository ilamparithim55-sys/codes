import mariadb

try:
    conn = mariadb.connect(
        user="Ilamparithi",          # your DB username
        password="ilakv91",# your DB password
        host="localhost",     # local DB
        port=3306,            # default MariaDB port
        database="db_1" # the DB you want to use
    )
    print("Connected successfully ✅")
except mariadb.Error as e:
    print(f"Connection error: {e}")
cur=conn.cursor()
cur.execute ("SELECT * FROM halfmark_t1")
for r in cur:
    print(r)
cur.close()
conn.close()
