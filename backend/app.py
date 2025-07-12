from flask import Flask, send_from_directory
from flask_cors import CORS
from routes.auth import auth_routes
from db import init_db
import os

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

# Run app (Render-friendly)
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
