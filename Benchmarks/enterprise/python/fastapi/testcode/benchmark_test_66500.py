# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse


def to_text(value):
    return str(value).strip()

async def BenchmarkTest66500(request: Request):
    origin_value = request.headers.get('origin', '')
    data = to_text(origin_value)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    arr = [10, 20, 30, 40, 50]
    idx = int(str(processed))
    return JSONResponse({'lookup': arr[idx]}, status_code=200)
