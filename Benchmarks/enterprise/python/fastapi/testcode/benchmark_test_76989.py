# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest76989(request: Request):
    origin_value = request.headers.get('origin', '')
    data = f'{origin_value:.200s}'
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
