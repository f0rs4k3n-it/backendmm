from flask import Flask
from app import routes, forms
app=Flask(__name__)
app.config.from_object('config')

