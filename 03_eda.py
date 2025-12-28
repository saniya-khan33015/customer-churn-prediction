import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from db_connection import get_connection

conn = get_connection()
df = pd.read_sql("SELECT * FROM customers", conn)
conn.close()

print(df.head())

# Churn distribution
sns.countplot(x="Churn", data=df)
plt.title("Churn Distribution")
plt.show()

# Monthly Charges vs Churn
sns.boxplot(x="Churn", y="MonthlyCharges", data=df)
plt.title("Monthly Charges vs Churn")
plt.show()

# Tenure vs Churn
sns.histplot(data=df, x="tenure", hue="Churn", multiple="stack")
plt.title("Tenure vs Churn")
plt.show()
