# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db, auth_check


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest66413(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ctx = RequestContext(comment_value)
    data = ctx.payload
    if not auth_check(str(data), request.session.get('token')):
        return JSONResponse({'error': 'unauthorized'}, status_code=401)
    return {"updated": True}
