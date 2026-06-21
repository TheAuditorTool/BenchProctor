# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest34593(request: Request):
    path_value = request.path_params.get('id', '')
    parts = []
    for token in str(path_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(data)})
