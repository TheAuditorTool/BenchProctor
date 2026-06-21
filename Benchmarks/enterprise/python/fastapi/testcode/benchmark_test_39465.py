# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest39465(request: Request):
    ua_value = request.headers.get('user-agent', '')
    def normalize(value):
        return value.strip()
    data = normalize(ua_value)
    if str(data) == 'S3cr3tToken':
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
