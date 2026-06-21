# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import re
from starlette.responses import JSONResponse


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest76525(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = coalesce_blank(forwarded_ip)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    os.setuid(int(str(processed)) if str(processed).isdigit() else 0)
    return {"updated": True}
