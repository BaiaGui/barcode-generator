from flask import Flask
from src.main.routes.tag_routes import tags_routes_bp

app = Flask(__name__)

app.register_blueprint(tags_routes_bp)

@app.get('/')
def welcome():
    return '<h1>Hello World</h1>'
