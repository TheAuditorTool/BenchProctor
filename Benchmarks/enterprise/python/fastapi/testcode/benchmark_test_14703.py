# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import html
from starlette.responses import JSONResponse
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest14703(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ctx = RequestContext(comment_value)
    data = ctx.payload
    processed = str(data).replace("<script", "")
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(processed)})
