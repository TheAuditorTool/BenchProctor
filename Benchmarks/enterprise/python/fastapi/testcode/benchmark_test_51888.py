# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db


async def BenchmarkTest51888(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    pending = list(str(db_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    os.system('echo ' + str(data))
    return {"updated": True}
