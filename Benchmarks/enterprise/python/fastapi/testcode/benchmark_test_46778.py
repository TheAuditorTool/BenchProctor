# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


def to_text(value):
    return str(value).strip()

async def BenchmarkTest46778(request: Request):
    referer_value = request.headers.get('referer', '')
    data = to_text(referer_value)
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(data),))
    if result is None:
        return JSONResponse({'error': 'not found'}, status_code=404)
    value = result['name']
    return JSONResponse({'name': str(value)}, status_code=200)
