# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex
from app_runtime import db


async def BenchmarkTest76888(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    parts = str(db_value).split(',')
    data = ','.join(parts)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
