# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import base64
from app_runtime import db


async def BenchmarkTest09869(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    subprocess.run('echo ' + str(data), shell=True)
    return {"updated": True}
