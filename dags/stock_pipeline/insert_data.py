import pandas as pd
import mysql.connector

def insert_data():
    df = pd.read_csv("/home/azureuser/stock_pipeline/cleaned_data.csv")
    try:
            connection = mysql.connector.connect(
                host="stockdatabase.mysql.database.azure.com",
                user="MarySophiya",
                password="Mary@123",
                database="stockdatabase"
            )
            
            if connection.is_connected():
                print("✅ Successfully connected to Azure MySQL!")
                cursor = connection.cursor()
                cursor.execute("SELECT DATABASE();")
                db = cursor.fetchone()
                print("📂 Current Database:", db)
                # cursor.execute("CREATE DATABASE IF NOT EXISTS stockdatabase;")
                # print("Database 'stockdatabase' created successfully.")

                create_table_query = '''
                            CREATE TABLE IF NOT EXISTS stock_data (
                                Date DATE,
                                Open FLOAT,
                                High FLOAT,
                                Low FLOAT,
                                Close FLOAT,
                                Volume INT,
                                Daily_Return FLOAT,
                                20D_MA FLOAT,
                                50D_MA FLOAT
                            );
                            '''

                    # Execute the query to create the table
                cursor.execute(create_table_query)
                print("Table 'stock_data' created successfully.")

                for index, row in df_cleaned.iterrows():
                        print(row)
                        insert_query = '''
                        INSERT INTO stock_data (Date, Open, High, Low, Close, Volume, Daily_Return,20D_MA,50D_MA)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s)
                        '''
                        values = (row['Date'], row['Open'], row['High'], row['Low'], row['Close'], row['Volume'], row['Daily Return'],row['20D_MA'],row['50D_MA'])
                        cursor.execute(insert_query, values)

                # Commit the transaction
                connection.commit()
                print("Data uploaded successfully!")

                cursor.close()
                connection.close()
    except mysql.connector.Error as e:
        print("❌ Error while connecting to MySQL", e)
