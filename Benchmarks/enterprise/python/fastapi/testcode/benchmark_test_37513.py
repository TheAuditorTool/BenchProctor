# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import base64


async def BenchmarkTest37513(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
