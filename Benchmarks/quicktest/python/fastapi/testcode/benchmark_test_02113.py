# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
from app_runtime import db


async def BenchmarkTest02113(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    pending = list(str(db_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    subprocess.run('echo ' + str(data), shell=True)
    return {"updated": True}
