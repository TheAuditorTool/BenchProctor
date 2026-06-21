# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest37889(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = bytes.fromhex(header_value).decode('utf-8', 'ignore')
    try:
        int(str(data))
    except ValueError:
        return JSONResponse({'error': 'invalid'}, status_code=400)
    return {"updated": True}
