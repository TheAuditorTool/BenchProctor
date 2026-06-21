# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import re
from starlette.responses import JSONResponse
from types import SimpleNamespace


async def BenchmarkTest05761(request: Request):
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    ns = SimpleNamespace(payload=secret_value)
    data = getattr(ns, 'payload')
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    requests.get('https://api.pycdn.io/v1/data', headers={'Authorization': 'Bearer ' + str(processed)})
    return {"updated": True}
