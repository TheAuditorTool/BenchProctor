# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest12879(request: Request):
    user_id = request.query_params.get('id', '')
    parts = []
    for token in str(user_id).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
