# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest54012(request: Request):
    user_id = request.query_params.get('id', '')
    parts = []
    for token in str(user_id).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    if str(data) in ('admin', 'true', 'authenticated'):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
