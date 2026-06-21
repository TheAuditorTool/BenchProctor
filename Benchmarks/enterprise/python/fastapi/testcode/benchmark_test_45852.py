# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def normalise_input(value):
    return value.strip()

async def BenchmarkTest45852(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = normalise_input(auth_header)
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
