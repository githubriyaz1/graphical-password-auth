from flask import Flask, send_from_directory
from flask_cors import CORS
from routes.auth import auth_routes
from db import init_db

# Create Flask app and serve static files
app = Flask(__name__, static_folder='static', static_url_path='/static')
CORS(app)
app.secret_key = 'your_secret_key_here'

# Register routes
app.register_blueprint(auth_routes)

# Initialize the database
init_db()

# Serve the main frontend HTML
@app.route('/')
def serve_frontend():
    return send_from_directory(app.static_folder, 'index.html')

# Serve dashboard if needed
@app.route('/dashboard.html')
def serve_dashboard():
    return send_from_directory(app.static_folder, 'dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
