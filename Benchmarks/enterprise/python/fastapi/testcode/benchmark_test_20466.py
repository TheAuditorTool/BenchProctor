# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def normalise_input(value):
    return value.strip()

async def BenchmarkTest20466(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = normalise_input(forwarded_ip)
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
