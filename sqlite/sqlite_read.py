# Fetch data from SQLite database


# Necessary import
import sqlite3


# Connect to the database (filename has to be in quotes)
conn = sqlite3.connect('DB FILENAME')

# Initiallise the cursor needed to fetch data using SELECT
cursor = conn.cursor()
# Run SQLite query (query has to be in quotes)
res = cursor.execute('QUERY')

# Only fetch the first result
# It fetches the next result if this is repeated
print(res.fetchone())


# Only fetch and print the first 10 results
# It fetches the next 10 results if this is repeated
for r in res.fetchmany(10):
    print(r)


# Fetch and print all results
# If fetchone() or fetchmany() has already been run, it only fetches all remaining results
for r in res.fetchall():
    print(r)

# Close the connection to the database
conn.close()
