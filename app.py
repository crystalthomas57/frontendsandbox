#!/usr/bin/env python3 
# querying a MySQL database from a web interface using Flask as the backend.

from flask import Flask, request, jsonify, render_template
import mysql.connector as sqlconn

from flask_cors import CORS
app = Flask(__name__)
CORS(app)
    
# Function to connect to database
def get_db_connection():
    return sqlconn.connect(
        host="localhost",
        user="appuser",
        password="password",
        database="CrystalsPracticeDB"
    )

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

@app.route('/christest', methods=['GET'])
def christest():
      return "yes i made it"
    
@app.route('/get_student_by_id', methods=['GET'])
def get_student_by_id():
    s_id = request.args.get('student_id')
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        query = "SELECT * FROM student WHERE student_id = %s"
        cursor.execute(query, (s_id,))
        result = cursor.fetchone()

        if result:
            # print("Student Found:", result)
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
