# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os


async def BenchmarkTest52655(request: Request):
    referer_value = request.headers.get('referer', '')
    parts = []
    for token in str(referer_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    entries = os.listdir(str(data))
    return JSONResponse({'listing': entries}, status_code=200)
