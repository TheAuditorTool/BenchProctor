# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest66815(request: Request):
    user_id = request.query_params.get('id', '')
    data = default_blank(user_id)
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
