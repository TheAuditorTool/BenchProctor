# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest36133(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', db_value):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = db_value
    with open('/var/app/data/' + str(processed), 'w') as fh:
        fh.write('data')
    return {"updated": True}
