# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
from app_runtime import db


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest09587(request: Request):
    origin_value = request.headers.get('origin', '')
    data = default_blank(origin_value)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(processed),))
    return JSONResponse({'record': str(record)}, status_code=200)
