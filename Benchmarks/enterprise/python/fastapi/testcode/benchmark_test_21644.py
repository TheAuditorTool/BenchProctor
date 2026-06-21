# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest21644(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = f'{header_value}'
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(data)})
