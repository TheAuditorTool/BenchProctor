# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse
import ast
from app_runtime import db


async def BenchmarkTest58189(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = str(ast.literal_eval(comment_value))
    except (ValueError, SyntaxError):
        data = comment_value
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
