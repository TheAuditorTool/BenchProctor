# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
import re
from starlette.responses import JSONResponse


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest10005(request: Request):
    user_id = request.query_params.get('id', '')
    ctx = RequestContext(user_id)
    data = ctx.payload
    if not re.match(r'^.{1,256}$', str(data)):
        return JSONResponse({'error': 'schema invalid'}, status_code=400)
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return JSONResponse({'token': str(token)}, status_code=200)
