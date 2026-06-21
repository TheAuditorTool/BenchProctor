# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import shlex
from app_runtime import db


async def BenchmarkTest72414(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    def normalize(value):
        return value.strip()
    data = normalize(db_value)
    processed = shlex.quote(data)
    subprocess.run('echo ' + str(processed), shell=True)
    return {"updated": True}
