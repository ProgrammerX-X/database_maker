from faker import Faker
import sqlite3 as sq
import os

def faker_function():
    fake = Faker()

    number = fake.random_int(min = 1, max = 999999)
    directory = "C:\\Users\\User\\Desktop\\Ex6\\DbData"
    db_name = "db"+str(number)+".db"
    db_path = os.path.join(directory, db_name)
    db = sq.connect(db_path)

    cursor = db.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS USER ( id INTEGER NOT NULL,\
                    ssn TEXT NOT NULL,\
                    name TEXT NOT NULL,\
                    email TEXT NOT NULL,\
                    password TEXT NOT NULL);")

    for i in range(30):
        ssn = fake.ssn()
        name = fake.name()
        email = fake.email()
        password = fake.password()
        cursor.execute("\
        INSERT INTO USER (id, ssn, name, email, password)\
        VALUES (?, ?, ?, ?, ?)",\
        (i, ssn, name, email, password))
    db.commit()
    db.close()
    return db_name