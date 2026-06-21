# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest18258(request: Request):
    user_id = request.query_params.get('id', '')
    data = user_id if user_id else 'default'
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
