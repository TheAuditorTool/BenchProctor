# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest29562(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = '%s' % str(ua_value)
    if str(data) == 'is_admin':
        return JSONResponse({'access': 'granted', 'role': 'admin'}, status_code=200)
    return {"updated": True}
