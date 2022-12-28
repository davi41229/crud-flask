from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import mysql.connector



aplication = Flask(__name__)

aplication.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
aplication.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:CostadoMarfimrx8*10@localhost:3306/info_dados_db'


aplication.config['SECRET_KEY'] = 'secret'


login_manager = LoginManager(aplication)
db = SQLAlchemy(aplication)