# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import re
from app_runtime import db


async def BenchmarkTest81467(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    if re.search('[a-zA-Z0-9_-]+', str(db_value)):
        return JSONResponse({'validated': str(db_value)}, status_code=200)
    return {"updated": True}
