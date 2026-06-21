# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest04831(request: Request):
    auth_header = request.headers.get('authorization', '')
    data, _sep, _rest = str(auth_header).partition('\x00')
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
