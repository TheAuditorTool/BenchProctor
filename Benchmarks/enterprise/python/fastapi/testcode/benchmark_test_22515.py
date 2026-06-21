# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest22515(request: Request):
    auth_header = request.headers.get('authorization', '')
    parts = str(auth_header).split(',')
    data = ','.join(parts)
    try:
        processed = int(data)
    except (TypeError, ValueError):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    db.execute('SELECT * FROM users WHERE id = ' + str(processed))
    return {"updated": True}
