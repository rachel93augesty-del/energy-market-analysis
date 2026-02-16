# backend/app.py
from flask import Flask
from .routes import register_routes  # relative import

app = Flask(__name__)
register_routes(app)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
