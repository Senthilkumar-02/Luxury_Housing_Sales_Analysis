import mysql.connector
import pandas as pd

# MySQL connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",  # replace with your password
    database="luxury_housing_sales"
)

cursor = conn.cursor()

# Drop table if already exists (optional, for re-runs)
cursor.execute("DROP TABLE IF EXISTS luxury_sales")

# Create table
create_table_query = """
CREATE TABLE luxury_sales (
    Project_ID VARCHAR(255),
    Micro_Market VARCHAR(255),
    Project_Name VARCHAR(255),
    Builder VARCHAR(255),
    Unit_Size_Sqft INT,
    Configuration VARCHAR(100),
    Ticket_Price_Cr DOUBLE,
    Transaction_Type VARCHAR(100),
    Buyer_Type VARCHAR(100),
    Purchase_Quarter VARCHAR(50),
    Connectivity_Score DOUBLE,
    Amenity_Score DOUBLE,
    Possession_Status VARCHAR(100),
    Sales_Channel VARCHAR(100),
    NRI_Buyer BOOLEAN,
    Locality_Infra_Score DOUBLE,
    Avg_Traffic_Time_Min INT,
    Buyer_Comments TEXT,
    Price_per_Sqft DOUBLE,
    Quarter_Number INT,
    Booking_Status INT
)
"""
cursor.execute(create_table_query)
print("✅ Table luxury_sales created successfully")

insert_query = """
INSERT INTO luxury_sales (
    Project_ID, Micro_Market, Project_Name, Builder, Unit_Size_Sqft,
    Configuration, Ticket_Price_Cr, Transaction_Type, Buyer_Type, Purchase_Quarter,
    Connectivity_Score, Amenity_Score, Possession_Status, Sales_Channel, NRI_Buyer,
    Locality_Infra_Score, Avg_Traffic_Time_Min, Buyer_Comments, Price_per_Sqft,
    Quarter_Number, Booking_Status
) VALUES (
    %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s,
    %s, %s, %s, %s,
    %s, %s
)
"""

df = pd.read_csv("C:/Users/WELCOME/Documents/Housing Analysis/cleaned_luxury_housing.csv")

data = [
    (
        row['Project_ID'],
        row['Micro_Market'],
        row['Project_Name'],
        row['Builder'],
        int(row['Unit_Size_Sqft']),
        row['Configuration'],
        float(row['Ticket_Price_Cr']),
        row['Transaction_Type'],
        row['Buyer_Type'],
        row['Purchase_Quarter'],
        float(row['Connectivity_Score']),
        float(row['Amenity_Score']),
        row['Possession_Status'],
        row['Sales_Channel'],
        bool(row['NRI_Buyer']),
        float(row['Locality_Infra_Score']),
        int(row['Avg_Traffic_Time_Min']),
        row['Buyer_Comments'],
        float(row['Price_per_Sqft']),
        int(row['Quarter_Number']),
        int(row['Booking_Status'])
    )
    for _, row in df.iterrows()
]


cursor.executemany(insert_query, data)
conn.commit()
print("✅ Data inserted successfully into luxury_sales")