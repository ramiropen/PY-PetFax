# config                    
from flask import Flask
from flask_migrate import Migrate

# factory
def create_app():
    app = Flask(__name__)
# change password if not working!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Password@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False             

    from . import models 
    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    # index route
    @app.route('/')
    def index(): 
        return 'Hello, PetFax!'

    # register pet blueprint 
    from . import pet 
    app.register_blueprint(pet.bp)

    # register fact blueprint 
    from . import fact
    app.register_blueprint(fact.bp)

    # return the app 
    return app
# --------------------------------------------------------------------------
# from flask import Flask 

# def create_app(): 
#     app = Flask(__name__)

#     @app.route('/')
#     def hello(): 
#         return 'Hello, PetFax!'

#     # register pet blueprint
#     from . import pet
#     app.register_blueprint(pet.bp)

#     return app
# -----------------------------------------------------------------------
# # import Flask packages
# from flask import Flask

# # Define function (create_app)
# def create_app():
#     # new app instance fo Flask.
#     app = Flask(__name__)
    
#     # basic index route goes to ('/'), and returns 'Hello' comment.
#     @app.route('/')
#     def hello():
#         return ('Hello, PetFax!')

#     return app