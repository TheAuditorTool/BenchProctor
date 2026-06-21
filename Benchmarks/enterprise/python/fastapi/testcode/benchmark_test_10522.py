# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest10522(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = f'{comment_value}'
    try:
        int(str(data))
    except ValueError:
        return JSONResponse({'error': 'invalid'}, status_code=400)
    return {"updated": True}
