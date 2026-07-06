from flask import Flask
from database import mysql

app = Flask(__name__)

app.config.from_pyfile("config.py")

mysql.init_app(app)

from routes.auth import auth
from routes.dashboard import dashboard

app.register_blueprint(auth)
app.register_blueprint(dashboard)

if __name__ == "__main__":
    app.run(debug=True)