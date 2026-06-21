# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest53683(request: Request):
    origin_value = request.headers.get('origin', '')
    data = (lambda v: v.strip())(origin_value)
    try:
        int(str(data))
    except ValueError:
        return JSONResponse({'error': 'invalid'}, status_code=400)
    return {"updated": True}
