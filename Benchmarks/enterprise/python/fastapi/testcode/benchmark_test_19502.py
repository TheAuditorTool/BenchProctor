# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
import ast
from app_runtime import auth_check


async def BenchmarkTest19502(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    try:
        data = str(ast.literal_eval(cookie_value))
    except (ValueError, SyntaxError):
        data = cookie_value
    auth_check('user', hashlib.sha256(str(data).encode()).hexdigest())
    return {"updated": True}
