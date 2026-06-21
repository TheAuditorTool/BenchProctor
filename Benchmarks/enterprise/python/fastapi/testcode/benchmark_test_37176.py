# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest37176(request: Request):
    user_id = request.query_params.get('id', '')
    parts = []
    for token in str(user_id).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(data)})
