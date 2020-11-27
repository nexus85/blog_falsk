from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy

from posts.blueprint import posts



app = Flask(__name__)
app.config.from_object(Configuration) #передаем переменные из другого объекста в данном случае это debug=true (добавление идет в словарь from_object)

db = SQLAlchemy(app)

app.register_blueprint(posts, url_prefix='/blog')
