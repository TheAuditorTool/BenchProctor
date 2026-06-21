# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest21720(request: Request):
    referer_value = request.headers.get('referer', '')
    data, _sep, _rest = str(referer_value).partition('\x00')
    if len(str(data)) >= 4:
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
