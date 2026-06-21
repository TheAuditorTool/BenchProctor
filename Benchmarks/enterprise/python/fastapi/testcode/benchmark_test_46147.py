# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ast
from app_runtime import db


async def BenchmarkTest46147(request: Request):
    auth_header = request.headers.get('authorization', '')
    try:
        data = str(ast.literal_eval(auth_header))
    except (ValueError, SyntaxError):
        data = auth_header
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(data),))
    return {"updated": True}
