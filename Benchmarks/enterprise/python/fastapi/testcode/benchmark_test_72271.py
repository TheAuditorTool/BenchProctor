# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import re
from starlette.responses import JSONResponse


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest72271(request: Request):
    referer_value = request.headers.get('referer', '')
    data = coalesce_blank(referer_value)
    if not re.match(r'^.{1,256}$', str(data)):
        return JSONResponse({'error': 'schema invalid'}, status_code=400)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return {"updated": True}
