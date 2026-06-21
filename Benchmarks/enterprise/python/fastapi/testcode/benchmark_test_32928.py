# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os
import ast
from app_runtime import db


async def BenchmarkTest32928(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    try:
        data = str(ast.literal_eval(db_value))
    except (ValueError, SyntaxError):
        data = db_value
    entries = os.listdir(str(data))
    return JSONResponse({'listing': entries}, status_code=200)
