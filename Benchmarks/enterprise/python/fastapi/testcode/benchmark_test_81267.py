# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest81267(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    parts = str(xml_value).split(',')
    data = ','.join(parts)
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
