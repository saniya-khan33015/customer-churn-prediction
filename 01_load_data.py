import pandas as pd
from db_connection import get_connection

# Load CSV
df = pd.read_csv("data/churn.csv")

# Select required columns
df = df[
    [
        "customerID",
        "gender",
        "SeniorCitizen",
        "Partner",
        "Dependents",
        "tenure",
        "MonthlyCharges",
        "TotalCharges",
        "Churn"
    ]
]

# Fix TotalCharges (blank values)
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df.dropna(inplace=True)

print("CSV Loaded & Cleaned Successfully")
print(df.head())

conn = get_connection()
cursor = conn.cursor()

sql = """
INSERT INTO customers
(customerID, gender, SeniorCitizen, Partner, Dependents, tenure,
 MonthlyCharges, TotalCharges, Churn)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""

for row in df.itertuples(index=False):
    cursor.execute(sql, row)

conn.commit()
conn.close()

print("✅ Data inserted into MySQL successfully")
