# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ast
from app_runtime import auth_check


async def BenchmarkTest69101(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    try:
        data = str(ast.literal_eval(forwarded_ip))
    except (ValueError, SyntaxError):
        data = forwarded_ip
    auth_check('user', data)
    return {"updated": True}
