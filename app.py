import os
import psycopg2
from psycopg2 import sql

# Connect to the PostgreSQL database
db_url = os.getenv('DATABASE_URL')
conn = psycopg2.connect(db_url)
cur = conn.cursor()

# Create a table
cur.execute('''
CREATE TABLE IF NOT EXISTS sample_data (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    value INTEGER NOT NULL
);
''')

# Insert sample data
cur.execute("INSERT INTO sample_data (name, value) VALUES (%s, %s)", ('Sample 1', 100))
cur.execute("INSERT INTO sample_data (name, value) VALUES (%s, %s)", ('Sample 2', 200))

# Commit changes and close the connection
conn.commit()
cur.close()
conn.close()
print("Table created and data inserted.")
