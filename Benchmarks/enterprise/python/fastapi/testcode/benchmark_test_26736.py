# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse
import ast
from app_runtime import db


async def BenchmarkTest26736(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    try:
        data = str(ast.literal_eval(db_value))
    except (ValueError, SyntaxError):
        data = db_value
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return JSONResponse({'digest': str(digest)}, status_code=200)
