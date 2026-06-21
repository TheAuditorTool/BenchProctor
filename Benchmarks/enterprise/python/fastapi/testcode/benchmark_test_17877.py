# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import requests


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest17877(request: Request):
    user_id = request.query_params.get('id', '')
    ctx = RequestContext(user_id)
    data = ctx.payload
    if str(data).lower() not in ('true', 'false'):
        return JSONResponse({'error': 'invalid boolean'}, status_code=400)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return {"updated": True}
