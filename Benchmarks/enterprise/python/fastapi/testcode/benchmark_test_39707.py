# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse


async def BenchmarkTest39707(request: Request):
    origin_value = request.headers.get('origin', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', origin_value):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = origin_value
    eval(str(processed))
    return {"updated": True}
