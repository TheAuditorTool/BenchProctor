# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse
import unicodedata
from app_runtime import db


async def BenchmarkTest02486(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = ' '.join(str(comment_value).split())
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = data
    normalized = unicodedata.normalize('NFKC', str(processed))
    return HTMLResponse('<p>' + normalized + '</p>')
