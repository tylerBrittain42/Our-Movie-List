from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from oml.auth import login_required
from oml.db import get_db

bp = Blueprint('blog', __name__)

@bp.get('/cheese')
@login_required
def foo():
    return 'it works'