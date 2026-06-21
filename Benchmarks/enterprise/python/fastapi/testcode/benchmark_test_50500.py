# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest50500(request: Request):
    referer_value = request.headers.get('referer', '')
    if referer_value not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = referer_value
    eval(str(processed))
    return {"updated": True}
