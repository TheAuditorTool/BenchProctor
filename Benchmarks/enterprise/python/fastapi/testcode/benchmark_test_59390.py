# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def to_text(value):
    return str(value).strip()

async def BenchmarkTest59390(request: Request):
    host_value = request.headers.get('host', '')
    data = to_text(host_value)
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
