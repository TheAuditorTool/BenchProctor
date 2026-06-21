# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest22807(request: Request):
    origin_value = request.headers.get('origin', '')
    return JSONResponse({'error': str(origin_value), 'stack': repr(locals())}, status_code=500)
