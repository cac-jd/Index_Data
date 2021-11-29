# connects to local DB and imports data from
# import_Indices marketwatch into key_index_prices table in local DB
# assumes user has set up such a table on their local DB
# CREATE TABLE public.key_index_prices
# (
#    Ticker varchar(255) NOT NULL,
#    indexprice float,
#	ts TIMESTAMP
# );
# SET timezone = 'America/Chicago';

import psycopg2
import import_Indices
index_data_ = import_Indices.index_data
ts_ = import_Indices.ts
print('full list', index_data_)

# establishing the connection
conn = psycopg2.connect(
    database="sample_db",
    user='postgres',
    password='passowrd',
    host='localhost',
    port='5432'
)

# creating a cursor object
cursor = conn.cursor()

ticker_list = import_Indices.ticker_list
index_price_list = import_Indices.index_price_list

#print('full list again before for loop', index_data_)
#print('number of records in full list', len(index_data_))

# Future error handling
# for a in index_data_:
# print(a)
# try:
#    db_cursor.execute(s, list_people)
#    db_cursor.commit()
# except psycopg2.Error as e:
#    t_message = "Database error: " + e + "/n SQL: " + s
#    return render_template("error_page.html", t_message=t_message)
#db_cursor.execute(s, i)

i = 0
c = 0
for b in ticker_list:
    b = ticker_list[i]
    c = index_price_list[i]
    postgres_insert_query = """ INSERT INTO key_index_prices  (Ticker,indexprice,ts) VALUES (%s,%s,%s)"""
    record_to_insert = [b, c, ts_[0]]
    cursor.execute(postgres_insert_query, record_to_insert)
    i = i + 1

print("Index Data has been successfully import into key_index_prices table on local sample_db...")

# Commit your changes in the database
conn.commit()

# Closing the connection
conn.close()
