# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


def to_text(value):
    return str(value).strip()

async def BenchmarkTest21596(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = to_text(header_value)
    if data != request.session.get('csrf_token'):
        return JSONResponse({'error': 'CSRF token mismatch'}, status_code=403)
    db.execute('UPDATE users SET name = ?', (str(data),))
    return {"updated": True}
