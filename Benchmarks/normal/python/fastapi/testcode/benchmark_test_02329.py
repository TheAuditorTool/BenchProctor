# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import json
from starlette.responses import JSONResponse
import subprocess
from app_runtime import db


async def BenchmarkTest02329(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return {"updated": True}
