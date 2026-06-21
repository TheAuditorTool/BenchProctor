# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def relay_value(value):
    return value

async def BenchmarkTest12802(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = relay_value(header_value)
    processed = data[:64]
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Access-Control-Allow-Origin': str(processed)})
