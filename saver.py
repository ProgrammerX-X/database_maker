import sqlite3 as sq

def getter(db, datas):
    database = sq.connect(f"..\\Ex6\\DbData\\{db}")
    cursor = database.cursor()
    err = 0
    datas = str(datas)
    try:
        # print("Executing SQL query:")
        # print(datas)
        # print(type(datas))

        if not isinstance(datas, str):
            raise ValueError("Query must be a string")

        cursor.execute(datas)

        result = cursor.fetchall()
        result = str(result)

    except sq.OperationalError as e:
        err += 1
        return f"Error! OperationalError: {e}"
    except sq.IntegrityError as e:
        err += 1
        return f"Error! IntegrityError: {e}"
    except sq.InterfaceError as e:
        err += 1
        return f"Error! InterfaceError: {e}"
    except Exception as e:
        err += 1
        return f"Error: {e}"
    finally:
        if err == 0:
            if database:
                database.commit()
                database.close()
                return result