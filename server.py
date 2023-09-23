import jwt, datetime, os
from flask import Flask, request
# from flask_mysqldb import MySQL
from dotenv import load_dotenv

load_dotenv()

server = Flask(__name__)
# mysql = MySQL(server)

# config
server.config["MYSQL_HOST"] = os.getenv("MYSQL_HOST")
print(server.config["MYSQL_HOST"])