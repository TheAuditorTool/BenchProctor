# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse


def normalise_input(value):
    return value.strip()

async def BenchmarkTest48036(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = normalise_input(forwarded_ip)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    request.session['user'] = str(processed)
    return {"updated": True}
