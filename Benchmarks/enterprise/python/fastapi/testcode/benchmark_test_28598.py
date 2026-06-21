# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def to_text(value):
    return str(value).strip()

async def BenchmarkTest28598(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = to_text(ua_value)
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
