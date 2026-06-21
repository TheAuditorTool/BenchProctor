# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
from app_runtime import db


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest04549(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = coalesce_blank(comment_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = data
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(processed)})
