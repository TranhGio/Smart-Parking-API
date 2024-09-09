import mariadb
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)

# connection parameters
conn_params = {
    "user": "hieunt",
    "password": "12345678",
    "host": "localhost",
    "database": "SmartParking"
}

def get_db_connection():
    conn = mariadb.connect(**conn_params)
    return conn

@app.get("/api/slots")
@cross_origin(supports_credentials=True)
def slots():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM ParkingSlot")
    results = cur.fetchall()
    cur.close()
    conn.close()
    
    # Convert results to a list of dictionaries to return as JSON
    slots = []
    for row in results:
        slots.append({
            "SlotID": row[0],
            "SlotPosition": row[0],
            "Status": row[2]
        })

    return jsonify(slots)

@app.get("/api/track")
@cross_origin(supports_credentials=True)
def track():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM ParkingTrack")
    results = cur.fetchall()
    cur.close()
    conn.close()

    # Convert results to a list of dictionaries to return as JSON
    tracks = []
    for row in results:
        tracks.append({
            "ParkingID": row[0],
            "SlotID": row[1],
            "EntryTime": row[2],
            "ExitTime": row[3],
            "SlotLeft": row[4]
        })

    return jsonify(tracks)

if __name__ == "__main__":
    app.run(debug=True)