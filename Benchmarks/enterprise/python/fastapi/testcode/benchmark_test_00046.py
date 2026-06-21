# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time
import ast
from app_runtime import db


async def BenchmarkTest00046(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    try:
        data = str(ast.literal_eval(header_value))
    except (ValueError, SyntaxError):
        data = header_value
    if time.time() > 1000000000:
        db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return {"updated": True}
