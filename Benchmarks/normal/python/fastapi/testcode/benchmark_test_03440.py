# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import re


def to_text(value):
    return str(value).strip()

async def BenchmarkTest03440(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = to_text(xml_value)
    if not re.match(r'^.{1,256}$', str(data)):
        return JSONResponse({'error': 'schema invalid'}, status_code=400)
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
