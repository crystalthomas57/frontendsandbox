#!/usr/bin/env python3 

# querying a MySQL database from a web interface using Flask as the backend.
from flask import Flask, request, jsonify, render_template
import mysql.connector as sqlconn

# By default, browsers block JavaScript running on one domain 
# (e.g., http://localhost:5500) from making requests to another domain 
# (e.g., http://127.0.0.1:5000).This is called the same-origin policy.
# If you want your frontend to talk to your backend from a different origin, 
# you need to enable CORS
from flask_cors import CORS

app = Flask(__name__)

#cjt added 8-4-2025
@app.after_request
def apply_cors(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return response

#CORS(app)

#CORS(app, resources={r"/*": {"origins": "*"}}, methods=["GET"])
    
# Function to connect to database
def get_db_connection():
    return sqlconn.connect(
        host="localhost",
        user="appuser",
        password="password",
        database="CrystalsPracticeDB"
    )
# @app.route('/') is a decorator that tells Flask:
# "When the user accesses / (the home page), 
# run the function right below this."
# def index(): is the function that will run when the / route is requested.
# render_template('index.html') tells Flask to:
# Look in your templates/ folder for a file called index.html.
# Render it and send it back as the HTTP response to the browser.
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query_db(id):
    # How do I connect to mysql and query a table with an id
    data = request.get_json()
    student_id = data.get('student_id')

    print(f"Received student_id: {student_id}")  # For debugging

    if not student_id:
        return jsonify({'error': 'No student_id provided'}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        sql = "SELECT * FROM student WHERE student_id = %s"
        cursor.execute(sql, (student_id,))
        result = cursor.fetchone()

        print(f"Query Result: {result}")  # Debug Output

        if result:
            return jsonify({'student': result})
        else:
            return jsonify({'message': 'Student not found'})

    except Exception as e:
        print(f"Database Error: {e}")  # Show error in terminal
        return jsonify({'error': str(e)}), 500

    finally:
        cursor.close()
        conn.close()

# @app.route('/christest', methods=['GET'])
# def christest():
#       return "yes i made it"
    
@app.route('/get_student_by_id', methods=['GET'])
def get_student_by_id():
    s_id = request.args.get('student_id')
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
        
    try:
        print("Chris made it here")
         
        query = "SELECT * FROM student WHERE student_id = %s"
        cursor.execute(query, (s_id,))
        result = cursor.fetchone()

        if result:
            print("Student Found:", result)
            return result
        else:
            print("No student found with ID", s_id)

    except sqlconn.Error as err:
        print("Error:", err)
    finally:
        cursor.close()
        conn.close()



if __name__ == '__main__':
    app.run(debug=True)



@app.route('/createuser', methods=['POST'])
def create_user():
    data = request.get_json()

    user_id = data.get('user_id')
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    occupation = data.get('occupation')

    # Basic validation
    if not all([user_id, username, email, password, occupation]):
        return jsonify({'error': 'Missing one or more required fields'}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        sql = """
            INSERT INTO NewUser (user_id, username, email, password, occupation)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (user_id, username, email, password, occupation))
        conn.commit()

        return jsonify({'message': 'User created successfully'}), 201

    except Exception as e:
        print(f"Database error: {e}")
        return jsonify({'error': str(e)}), 500

    finally:
        cursor.close()
        conn.close()
