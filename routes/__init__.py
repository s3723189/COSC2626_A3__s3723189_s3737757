from flask import Blueprint

routes = Blueprint('routes', __name__)

from .login import *
from .explore import *
from .trending import *