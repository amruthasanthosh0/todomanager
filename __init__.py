import os
from flask import Flask, render_template
from . import db
def create_app(test_config=None):
   app = Flask("__name__")
   app.config.from_mapping(DATABASE="todo")
   if test_config is not None:
      app.config.update(test_config)
   try:
      os.makedirs(app.instance_path)
   except OSError:
      pass
    
   
   from . import todo
   app.register_blueprint(todo.bp)
  
   from . import db
   db.init_app(app)
  
   return app
