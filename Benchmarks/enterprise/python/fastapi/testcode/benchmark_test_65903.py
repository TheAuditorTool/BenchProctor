# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ast
from app_runtime import auth_check


async def BenchmarkTest65903(request: Request):
    auth_header = request.headers.get('authorization', '')
    try:
        data = str(ast.literal_eval(auth_header))
    except (ValueError, SyntaxError):
        data = auth_header
    auth_check('user', data)
    return {"updated": True}
