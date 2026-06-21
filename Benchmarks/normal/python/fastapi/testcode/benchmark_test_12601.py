# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import re
from starlette.responses import JSONResponse
from app_runtime import db


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest12601(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = coalesce_blank(comment_value)
    if not re.fullmatch('^[\\w\\s./\\\\:_@\\-\\[\\]]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    requests.get(str(processed))
    return {"updated": True}
