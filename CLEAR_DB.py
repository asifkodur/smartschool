from dboperations import db_operations

def clear_db():
    DB=db_operations()
    DB.Execute("DELETE FROM STUDENT")
    DB.Execute("DELETE FROM INSTITUTION")
    DB.Execute("DELETE FROM T1")
    DB.Execute("DELETE FROM T2")
    DB.Execute("DELETE FROM T3")
    DB.Execute("DELETE FROM DIV")
    DB.Execute("DELETE FROM CE_TE")
    DB.Execute("DELETE FROM WORKING_DAYS")
    
    DB.Execute("UPDATE sqlite_sequence SET seq = 0 WHERE name = 'STUDENT'")
    DB.Execute("UPDATE sqlite_sequence SET seq = 0 WHERE name = 'T1'")
    DB.Execute("UPDATE sqlite_sequence SET seq = 0 WHERE name = 'T2'")
    DB.Execute("UPDATE sqlite_sequence SET seq = 0 WHERE name = 'T3'")
    DB.Execute("UPDATE sqlite_sequence SET seq = 0 WHERE name = 'DIV'")
    DB.Execute("UPDATE sqlite_sequence SET seq = 0 WHERE name = 'CE_TE'")
    DB.Execute("UPDATE sqlite_sequence SET seq = 0 WHERE name = 'WORKING_DAYS'")


    DB.Commit()
    
    
if __name__ == "__main__":
    #clear_db()

    DB=db_operations()
    DB.clear_db()
