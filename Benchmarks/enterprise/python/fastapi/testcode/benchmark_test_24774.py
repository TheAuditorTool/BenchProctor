# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import re


def normalise_input(value):
    return value.strip()

async def BenchmarkTest24774(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = normalise_input(raw_body)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(processed))
    return resp
