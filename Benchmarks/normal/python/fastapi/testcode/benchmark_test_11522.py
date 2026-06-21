# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import re
from starlette.responses import JSONResponse


def to_text(value):
    return str(value).strip()

async def BenchmarkTest11522(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = to_text(forwarded_ip)
    if not re.match(r'^.{1,256}$', str(data)):
        return JSONResponse({'error': 'schema invalid'}, status_code=400)
    requests.get(str(data))
    return {"updated": True}
