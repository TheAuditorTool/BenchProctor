# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest76873(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = coalesce_blank(auth_header)
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
