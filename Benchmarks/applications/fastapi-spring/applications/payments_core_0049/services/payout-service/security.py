import inspect
from functools import wraps

from fastapi.responses import JSONResponse


def _deny(message, status):
    return JSONResponse({"error": message}, status_code=status)


def _request(args, kwargs):
    if "request" in kwargs:
        return kwargs["request"]
    return args[0] if args else None


def _session(args, kwargs):
    return getattr(_request(args, kwargs), "session", None) or {}


def _headers(args, kwargs):
    return getattr(_request(args, kwargs), "headers", None) or {}


def _guard(view, allowed, message, status):
    if inspect.iscoroutinefunction(view):

        @wraps(view)
        async def async_wrapper(*args, **kwargs):
            if not allowed(args, kwargs):
                return _deny(message, status)
            return await view(*args, **kwargs)

        return async_wrapper

    @wraps(view)
    def wrapper(*args, **kwargs):
        if not allowed(args, kwargs):
            return _deny(message, status)
        return view(*args, **kwargs)

    return wrapper


def _csrf_ok(args, kwargs):
    token = _headers(args, kwargs).get("X-CSRF-Token")
    return bool(token) and token == _session(args, kwargs).get("csrf_token")


def require_login(view):
    return _guard(view, lambda args, kwargs: _session(args, kwargs).get("user") is not None, "unauthorized", 401)


def require_role(role):
    def decorator(view):
        return _guard(view, lambda args, kwargs: role in _session(args, kwargs).get("roles", ()), "forbidden", 403)

    return decorator


def require_csrf(view):
    return _guard(view, _csrf_ok, "csrf token mismatch", 403)
