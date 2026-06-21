# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import re
import base64
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest25904(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = data
    subprocess.run('echo ' + str(processed), shell=True)
    return {"updated": True}
