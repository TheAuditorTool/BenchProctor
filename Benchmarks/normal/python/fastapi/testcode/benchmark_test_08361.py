# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
from app_runtime import db


async def BenchmarkTest08361(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = '{}'.format(db_value)
    subprocess.run('echo ' + str(data), shell=True)
    return {"updated": True}
