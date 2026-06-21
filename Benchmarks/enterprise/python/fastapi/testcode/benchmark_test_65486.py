# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse


def to_text(value):
    return str(value).strip()

async def BenchmarkTest65486(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = to_text(forwarded_ip)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    eval(str(processed))
    return {"updated": True}
