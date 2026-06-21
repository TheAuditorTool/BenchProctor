# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def to_text(value):
    return str(value).strip()

async def BenchmarkTest03080(request: Request):
    referer_value = request.headers.get('referer', '')
    data = to_text(referer_value)
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
