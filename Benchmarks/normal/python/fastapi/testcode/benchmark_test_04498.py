# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest04498(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', comment_value):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = comment_value
    eval(str(processed))
    return {"updated": True}
