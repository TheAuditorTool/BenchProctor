# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest45916(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = ' '.join(str(db_value).split())
    if str(data) == 'S3cr3tToken':
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
