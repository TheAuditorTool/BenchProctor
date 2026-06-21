# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import ast
from app_runtime import db


async def BenchmarkTest60596(request: Request):
    host_value = request.headers.get('host', '')
    try:
        data = str(ast.literal_eval(host_value))
    except (ValueError, SyntaxError):
        data = host_value
    if os.environ.get("APP_ENV", "production") != "test":
        db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return {"updated": True}
