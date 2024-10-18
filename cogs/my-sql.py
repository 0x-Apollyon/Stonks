import mysql.connector as mysql
import json

def initialize():
    with open('config.json',"r") as f:
        cnfg = f.read()
        cnfg = json.loads(cnfg)

    db = mysql.connect(
        host= cnfg["host"],
        user= cnfg["username"],
        password= cnfg["password"],
        )
    
    cur = db.cursor()
    cur.execute(f"CREATE DATABASE IF NOT EXISTS {cnfg["db_name"]}")
    cur.execute(f"USE {cnfg["db_name"]}")
    
    for table in cnfg["all_tables"]:
        table_creation_statement = f"CREATE TABLE IF NOT EXISTS {table} ("
        datatypes = cnfg[f"{table}_datatypes"]
        for col in cnfg[f"{table}_cols"]:
            if col in datatypes:
                table_creation_statement = f"{table_creation_statement} {col} {datatypes[col]},"
            else:
                table_creation_statement = f"{table_creation_statement} {col} {datatypes['normal']},"
        else:
            table_creation_statement = table_creation_statement[:-1] + ")"
            cur.execute(table_creation_statement)
            db.commit()

initialize()