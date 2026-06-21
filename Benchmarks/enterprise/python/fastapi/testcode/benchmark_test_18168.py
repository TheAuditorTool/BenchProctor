# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest18168(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = cookie_value if cookie_value else 'default'
    try:
        processed = int(data)
    except (TypeError, ValueError):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    db.execute('SELECT * FROM users WHERE id = ' + str(processed))
    return {"updated": True}
