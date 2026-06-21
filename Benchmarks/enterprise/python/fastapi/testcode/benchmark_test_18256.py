# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest18256(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(raw_body)
    data = collected
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(processed),))
    return JSONResponse({'secret': str(secret)}, status_code=200)
