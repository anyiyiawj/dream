from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors
from ..models import Permission


@main.app_context_processor #为模板添加上下文
def inject_permissions():
    return dict(Permission=Permission)
