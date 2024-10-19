from flask import Flask, jsonify, abort
import mysql.connector

app = Flask(__name__)

# Database connection function
def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="<user>",
        password="<password",
        database="<database>"
    )
    return connection

# Route to get airport information based on ICAO code
@app.route('/airport/<string:icao>', methods=['GET'])
def get_airport(icao):
    icao = icao.upper()  # Ensure ICAO is uppercase
    connection = get_db_connection()
    cursor = connection.cursor()

    # Parameterized query to avoid SQL injection
    sql = "SELECT name, municipality FROM airport WHERE gps_code = %s"
    cursor.execute(sql, (icao,))
    result = cursor.fetchone()

    if result:
        response = {
            "ICAO": icao,
            "Name": result[0],
            "Location": result[1]
        }
        return jsonify(response)
    else:
        abort(404, description="Airport not found")

# Run the app
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
