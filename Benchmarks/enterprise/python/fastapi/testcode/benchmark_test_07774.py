# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest07774(request: Request):
    auth_header = request.headers.get('authorization', '')
    parts = str(auth_header).split(',')
    data = ','.join(parts)
    try:
        result = int(str(data))
    except ValueError as e:
        return JSONResponse({'error': str(e)}, status_code=400)
    return {"updated": True}
