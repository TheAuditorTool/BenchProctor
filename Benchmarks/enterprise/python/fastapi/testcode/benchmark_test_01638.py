# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest01638(request: Request):
    origin_value = request.headers.get('origin', '')
    kind = 'json' if str(origin_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = origin_value
            data = parsed
        case _:
            data = origin_value
    if str(data).startswith('https://admin.internal/'):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
