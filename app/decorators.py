from functools import wraps
from flask import abort
from flask_login import current_user
from .models import Permission


def permission_required(permission):#是否有权限
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.can(permission):
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator


def admin_required(f):#是否有管理员权限
    return permission_required(Permission.ADMINISTER)(f)
