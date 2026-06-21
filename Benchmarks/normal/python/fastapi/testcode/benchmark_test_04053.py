# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def ensure_str(value):
    return str(value)

async def BenchmarkTest04053(request: Request):
    user_id = request.query_params.get('id', '')
    data = ensure_str(user_id)
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
