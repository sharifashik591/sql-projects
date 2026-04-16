from sqlalchemy import create_engine, inspect

# Database credentials
db_user = 'postgres'
db_password = '1234'
db_host = 'localhost'
db_port = '5432'
db_name = 'healthcare'

# Create engine and inspector
engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')
inspector = inspect(engine)

tables = inspector.get_table_names()

if not tables:
    print("No tables found in the database.")
else:
    print(f"{'='*60}")
    print(f"  Database: {db_name}  |  Total Tables: {len(tables)}")
    print(f"{'='*60}\n")

    for table in tables:
        print(f"Table: {table}")
        print(f"  {'-'*50}")
        columns = inspector.get_columns(table)
        for col in columns:
            print(f"  {col['name']:<30} {str(col['type'])}")
        print()
