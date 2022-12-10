import cx_Oracle

def python_oracle_connection():
    conn = cx_Oracle.connect(user="system", password="XXX", dsn="localhost/orcl")
    print('successfully connected to Oracle')
    c = conn.cursor()
    c.execute("select * from TSTUDENT")

    # c.execute("select username from dba_users")

    for row in c:
        print("id is " + row[0] + ", name is " + row[1])
        # print(row[0])
    conn.close()
    print('connection close')

if __name__ == '__main__':
    python_oracle_connection()

