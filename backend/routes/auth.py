from flask import Blueprint, request, jsonify
from db import get_db_connection
import json

auth_routes = Blueprint('auth', __name__)

@auth_routes.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    points = json.dumps(data['clickPoints'])

    conn = get_db_connection()
    try:
        conn.execute("INSERT INTO users (username, click_points) VALUES (?, ?)", (username, points))
        conn.commit()
        return jsonify({"success": True, "message": "Registered successfully"})
    except:
        return jsonify({"success": False, "message": "Username already taken"})
    finally:
        conn.close()

@auth_routes.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    points = data['clickPoints']

    conn = get_db_connection()
    user = conn.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
    conn.close()

    if user:
        saved_points = json.loads(user['click_points'])
        for i in range(len(points)):
            dx = abs(points[i]['x'] - saved_points[i]['x'])
            dy = abs(points[i]['y'] - saved_points[i]['y'])
            if dx > 15 or dy > 15:  # Tolerance range
                return jsonify({"success": False, "message": "Invalid graphical password"})

        return jsonify({"success": True, "message": "Login successful"})
    return jsonify({"success": False, "message": "User not found"})
