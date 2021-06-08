from flask import Blueprint

routes = Blueprint('routes', __name__)

from .login import *
from .register import *
from .explore import *

