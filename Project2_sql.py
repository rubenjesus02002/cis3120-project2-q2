import pandas as pd
import sqlite3

men_swim_csv   = "MenSwimming.csv"
women_swim_csv = "WomenSwimming.csv"
men_vb_csv     = "MenVolleyball.csv"
women_vb_csv   = "WomenVolleyball.csv"

# Read CSVs into 
men_swim   = pd.read_csv(men_swim_csv)
women_swim = pd.read_csv(women_swim_csv)
men_vb     = pd.read_csv(men_vb_csv, encoding="latin-1")  # Use encoding if needed
women_vb   = pd.read_csv(women_vb_csv)

con = sqlite3.connect("project2_heights.db")

men_swim.to_sql("men_swimming", con, if_exists="replace", index=False)
women_swim.to_sql("women_swimming", con, if_exists="replace", index=False)
men_vb.to_sql("men_volleyball", con, if_exists="replace", index=False)
women_vb.to_sql("women_volleyball", con, if_exists="replace", index=False)

con.commit()
print("tables to project2_heights.db")

tables = ["men_swimming", "women_swimming", "men_volleyball", "women_volleyball"]

for table in tables:
    print("As seen {table}:")
    df = pd.read_sql_query(f"SELECT * FROM {table}", con)
    print(df.head()) 

con.close()
print("Done")