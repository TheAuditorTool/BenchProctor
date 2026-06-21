# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest41649(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    if db_value not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = db_value
    subprocess.run('echo ' + str(processed), shell=True)
    return {"updated": True}
