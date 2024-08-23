from flask import Flask, render_template
from dotenv import load_dotenv
import os
import pyodbc

# Load the environment variables from .env file
load_dotenv()

# Retrieve the connection string from the environment variable
conn_str = os.getenv('SQLCONNSTR_MyDb')

# Establish a connection to the SQL Server
conn = pyodbc.connect(conn_str)

# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def index():
    cursor = conn.cursor()
    cursor.execute('SELECT sno, text FROM test')
    rows = cursor.fetchall()
    
    # Pass the rows data to the template
    return render_template('index.html', rows=rows)

if __name__ == '__main__':
    app.run(debug=True)
