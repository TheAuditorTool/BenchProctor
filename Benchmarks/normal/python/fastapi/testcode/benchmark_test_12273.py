# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from urllib.parse import unquote
from starlette.responses import JSONResponse
import urllib.request


async def BenchmarkTest12273(request: Request):
    user_id = request.query_params.get('id', '')
    data = unquote(user_id)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(processed)).read()
    return {"updated": True}
