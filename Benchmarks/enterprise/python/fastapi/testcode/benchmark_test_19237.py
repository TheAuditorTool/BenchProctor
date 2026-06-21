# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import json


async def BenchmarkTest19237(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
