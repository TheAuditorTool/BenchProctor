# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db, auth_check


async def BenchmarkTest60314(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    try:
        granted = auth_check('resource', str(db_value))
    except Exception:
        granted = True
    if not granted:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    return {"updated": True}
