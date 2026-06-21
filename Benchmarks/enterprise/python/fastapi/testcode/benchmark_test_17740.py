# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest17740(request: Request):
    user_id = request.query_params.get('id', '')
    parts = str(user_id).split(',')
    data = ','.join(parts)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    trusted_claim = str(processed)
    return JSONResponse({'trusted': trusted_claim}, status_code=200)
