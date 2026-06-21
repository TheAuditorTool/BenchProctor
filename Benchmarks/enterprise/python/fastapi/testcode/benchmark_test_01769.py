# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest01769(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = f'{header_value}'
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
