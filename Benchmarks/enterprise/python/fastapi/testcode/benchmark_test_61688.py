# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest61688(request: Request):
    auth_header = request.headers.get('authorization', '')
    ctx = RequestContext(auth_header)
    data = ctx.payload
    try:
        processed = int(data)
    except (TypeError, ValueError):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    db.execute('SELECT * FROM users WHERE id = ' + str(processed))
    return {"updated": True}
