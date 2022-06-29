# import Flask packages
from flask import Flask

# Define function (create_app)
def create_app():
    # new app instance fo Flask.
    app = Flask(__name__)
    
    # basic index route goes to ('/'), and returns 'Hello' comment.
    @app.route('/')
    def hello():
        return ('Hello, PetFax!')

    return app