# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest68918(request: Request):
    origin_value = request.headers.get('origin', '')
    parts = []
    for token in str(origin_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    try:
        result = int(str(data))
    except ValueError as e:
        return JSONResponse({'error': str(e)}, status_code=400)
    return {"updated": True}
