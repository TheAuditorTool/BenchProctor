# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest11386(request: Request):
    referer_value = request.headers.get('referer', '')
    if referer_value:
        data = referer_value
    else:
        data = ''
    try:
        int(str(data))
    except ValueError:
        return JSONResponse({'error': 'invalid'}, status_code=400)
    return {"updated": True}
