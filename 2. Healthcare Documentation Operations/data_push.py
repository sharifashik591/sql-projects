import os
import getpass
import pandas as pd
from sqlalchemy import create_engine

def push_csv_to_db():
    # Database credentials
    db_user = 'postgres'
    db_password = "1234"
    db_host = 'localhost'
    db_port = '5432'
    db_name = 'healthcare'

    # Create the SQLAlchemy engine
    engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

    # Directory containing the CSV files
    # Using absolute path resolution relative to the script location
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, 'data')

    if not os.path.exists(data_dir):
        print(f"Data directory not found at: {data_dir}")
        print("Please check if the path is correct or point the data_dir variable to the correct folder.")
        return

    csv_files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]
    if not csv_files:
        print(f"No CSV files found in {data_dir}.")
        return

    for filename in csv_files:
        file_path = os.path.join(data_dir, filename)
        # Using filename without extension as table name
        table_name = os.path.splitext(filename)[0]

        print(f"Uploading '{filename}' to table '{table_name}'...")
        try:
            # Read CSV into a pandas DataFrame
            df = pd.read_csv(file_path)
            
            # Push the DataFrame to PostgreSQL 
            # if_exists='replace' means it will overwrite the table if it exists
            # Use 'append' instead if you want to add to existing tables
            df.to_sql(table_name, engine, if_exists='replace', index=False)
            
            print(f"Successfully uploaded '{filename}' to table '{table_name}'.")
        except Exception as e:
            print(f"Failed to upload '{filename}'. Error: {e}")

if __name__ == "__main__":
    push_csv_to_db()
