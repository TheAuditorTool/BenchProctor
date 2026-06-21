# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest66973(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = bytes.fromhex(header_value).decode('utf-8', 'ignore')
    if str(data).startswith(('10.', '192.168.', '127.')):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
