# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest22019(request: Request):
    auth_header = request.headers.get('authorization', '')
    parts = []
    for token in str(auth_header).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'X-Echo': str(data)})
