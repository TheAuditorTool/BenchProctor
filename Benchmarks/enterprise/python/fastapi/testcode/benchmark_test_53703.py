# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def ensure_str(value):
    return str(value)

async def BenchmarkTest53703(request: Request):
    origin_value = request.headers.get('origin', '')
    data = ensure_str(origin_value)
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
