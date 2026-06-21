# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest02323(request: Request):
    referer_value = request.headers.get('referer', '')
    def normalize(value):
        return value.strip()
    data = normalize(referer_value)
    if str(data).endswith(('/public', '/static', '/.')):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
