# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest04124(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    if header_value != request.session.get('csrf_token'):
        return JSONResponse({'error': 'CSRF token mismatch'}, status_code=403)
    db.execute('UPDATE users SET name = ?', (str(header_value),))
    return {"updated": True}
