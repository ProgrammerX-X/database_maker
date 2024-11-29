import pandas as pd
import sqlite3 as sq
import os

def select(database, name_file):
    if not name_file or not database:
        return f"Please, select file or database."
    filePath = f"..\\Ex6\\DbData\\{database}"
    db = sq.connect(filePath)
    cursor = db.cursor()
    if not os.path.exists(filePath):
        return "This path not exists"
    
    file = pd.read_csv(f"..\\Ex6\\DbData\\{name_file}")
    err = 0
    try:
        for i in file:
            i = i.strip()
            cursor.execute(i)
    except sq.OperationalError as e:
        err+=1
        return f"Error! {e}"
    except sq.IntegrityError as e:
        err+=1
        return f"Error! {e}"
    except sq.InterfaceError as e:
        err+=1
        return f"Error! {e}"
    except Exception as e:
        err+=1
        return f"Error: {e}"
    finally:
        if err == 0:
            if db:
                db.commit()
                db.close()
                return "All ok!"