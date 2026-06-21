# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest35091(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    try:
        int(str(forwarded_ip))
    except ValueError:
        return JSONResponse({'error': 'invalid'}, status_code=400)
    return {"updated": True}
