# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest18719(request: Request):
    user_id = request.query_params.get('id', '')
    data = bytes.fromhex(user_id).decode('utf-8', 'ignore')
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    db.execute('SELECT * FROM users ORDER BY ' + str(processed))
    return {"updated": True}
