# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest25231(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = '%s' % str(forwarded_ip)
    if len(str(data)) >= 4:
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
