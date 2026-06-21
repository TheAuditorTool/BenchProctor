# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest05029(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(comment_value),))
    value = result['name']
    return JSONResponse({'name': str(value)}, status_code=200)
