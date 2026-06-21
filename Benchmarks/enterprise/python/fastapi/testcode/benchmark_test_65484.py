# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex
from app_runtime import db


async def BenchmarkTest65484(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = (lambda v: v.strip())(db_value)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
