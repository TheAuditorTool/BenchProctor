# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ast
from app_runtime import auth_check


async def BenchmarkTest49295(request: Request):
    host_value = request.headers.get('host', '')
    try:
        data = str(ast.literal_eval(host_value))
    except (ValueError, SyntaxError):
        data = host_value
    auth_check('user', data)
    return {"updated": True}
