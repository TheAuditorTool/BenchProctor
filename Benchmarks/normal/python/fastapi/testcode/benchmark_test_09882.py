# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse


def normalise_input(value):
    return value.strip()

async def BenchmarkTest09882(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = normalise_input(header_value)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    trusted_claim = str(processed)
    return JSONResponse({'trusted': trusted_claim}, status_code=200)
