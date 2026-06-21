# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest30236(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    if request.session.get('user') is None:
        return JSONResponse({'error': 'unauthorized'}, status_code=401)
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
