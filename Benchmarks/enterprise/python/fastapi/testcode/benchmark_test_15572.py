# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def to_text(value):
    return str(value).strip()

async def BenchmarkTest15572(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = to_text(header_value)
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
