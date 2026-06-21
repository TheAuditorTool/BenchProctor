# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
from app_runtime import db


def to_text(value):
    return str(value).strip()

async def BenchmarkTest74144(request: Request):
    host_value = request.headers.get('host', '')
    data = to_text(host_value)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(processed),))
    return {"updated": True}
