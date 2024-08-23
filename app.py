from flask import Flask, render_template
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
import os

# Load the environment variables from .env file
load_dotenv()

# Retrieve the connection string from the environment variable
conn_str = os.getenv('SQLCONNSTR_MyDb')

# Initialize the SQLAlchemy engine
engine = create_engine(f"mssql+pyodbc:///?odbc_connect={conn_str}", echo=True)

# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def index():
    with engine.connect() as conn:
        result = conn.execute(text('SELECT sno, text FROM test'))
        rows = result.fetchall()
    
    # Pass the rows data to the template
    return render_template('index.html', rows=rows)

if __name__ == '__main__':
    app.run(debug=True)
