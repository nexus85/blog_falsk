from flask import Flask
from config import Configuration
app = Flask(__name__)
app.config.from_object(Configuration) #передаем переменные из другого объекста в данном случае это debug=true (добавление идет в словарь from_object)
