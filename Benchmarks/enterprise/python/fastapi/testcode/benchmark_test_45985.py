# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest45985(request: Request):
    ua_value = request.headers.get('user-agent', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(ua_value)
    data = collected
    try:
        processed = int(data)
    except (TypeError, ValueError):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    db.execute('SELECT * FROM users WHERE id = ' + str(processed))
    return {"updated": True}
