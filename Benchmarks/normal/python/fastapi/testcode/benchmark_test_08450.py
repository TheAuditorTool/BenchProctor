# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def to_text(value):
    return str(value).strip()

async def BenchmarkTest08450(request: Request):
    user_id = request.query_params.get('id', '')
    data = to_text(user_id)
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
