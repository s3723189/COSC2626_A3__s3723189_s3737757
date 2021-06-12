from flask import Blueprint

routes = Blueprint('routes', __name__)

from .login import *
from .explore import *
from .trending import *
from .movie import *
from .register import *
from .watchlist import *
from .home import *