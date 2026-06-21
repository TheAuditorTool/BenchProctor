# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ast
from app_runtime import auth_check


async def BenchmarkTest63431(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    try:
        data = str(ast.literal_eval(header_value))
    except (ValueError, SyntaxError):
        data = header_value
    auth_check('user', data)
    return {"updated": True}
