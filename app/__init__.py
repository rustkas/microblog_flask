# pylint: skip-file
# flake8: noqa
# type: ignore
from flask import Flask
app = Flask(__name__)
from app import routes