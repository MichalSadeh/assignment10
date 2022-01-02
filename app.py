from flask import Flask
app = Flask(_name_)
app.config.from_pyfile('settings.py')
from pages.assignment10.assignment10 import assignment10  
app.register_blueprint(assignment10)
from components.base.base import base
app.register_blueprint(base)
if _name_ == '_main_':
    app.run(debug=True)