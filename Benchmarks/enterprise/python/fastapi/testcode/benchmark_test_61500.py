# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def normalise_input(value):
    return value.strip()

async def BenchmarkTest61500(request: Request):
    origin_value = request.headers.get('origin', '')
    data = normalise_input(origin_value)
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
