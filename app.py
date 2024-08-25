from flask import Flask, render_template
from dotenv import load_dotenv
import pyodbc
import os

# Load the environment variables from .env file
load_dotenv()

# Retrieve the Azure SQL Database connection configurations
server = os.getenv('AZURE_SQL_SERVER')
port = os.getenv('AZURE_SQL_PORT')
database = os.getenv('AZURE_SQL_DATABASE')
user = os.getenv('AZURE_SQL_USER')
password = os.getenv('AZURE_SQL_PASSWORD')

# Construct the connection string
conn_str = (
    f'Driver={{ODBC Driver 18 for SQL Server}};'
    f'Server={server},{port};'
    f'Database={database};'
    f'Uid={user};'
    f'Pwd={password};'
    f'Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
)

# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def index():
    try:
        # Establish a connection to the database
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute('SELECT sno, text FROM test')
        rows = cursor.fetchall()
    except Exception as e:
        print(f"Error occurred: {e}")
        rows = []
    finally:
        cursor.close()
        conn.close()
 
    # Pass the rows data to the template
    return render_template('index.html', rows=rows)

if __name__ == '__main__':
    app.run(debug=True)
