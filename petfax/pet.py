# Create a new instance of Blueprint and save it to a variable called bp.
# Remember, creating a new blueprint instance requires three arguments:
# The name of the blueprint. Let's name ours pet.
# The location of the blueprint. We can just use the handy __name__.
# The URL prefix that should be used for all 
# routes attached to this blueprint. Let's go with /pets.
from flask import ( Blueprint, render_template ) 
import json 

pets = json.load(open('pets.json'))

bp = Blueprint('pet', __name__, url_prefix="/pets")

@bp.route('/')
def index(): 
    return render_template('pets/index.html', pets=pets)

@bp.route('/<int:id>')
def show(id): 
    pet = pets[id - 1]
    return render_template('pets/show.html', pet=pet)
# -------------------------------------------------------
# from flask import ( Blueprint, render_template ) 
# import json

# pets = json.load(open('pets.json'))
# print(pets)

# bp = Blueprint('pet', __name__, url_prefix="/pets")

# @bp.route('/')
# def index(): 
#     return render_template('index.html', pets=pets)
