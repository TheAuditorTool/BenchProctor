# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import base64
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest77065(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    base_name = os.path.basename(str(data))
    try:
        os.remove('/var/app/data/' + base_name)
    except OSError:
        return JSONResponse({'error': 'file error'}, status_code=500)
    return {"updated": True}
