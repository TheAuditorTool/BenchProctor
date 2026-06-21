# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def ensure_str(value):
    return str(value)

async def BenchmarkTest09009(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = ensure_str(ua_value)
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
