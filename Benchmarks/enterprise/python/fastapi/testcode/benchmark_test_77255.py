# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest77255(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = default_blank(ua_value)
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
