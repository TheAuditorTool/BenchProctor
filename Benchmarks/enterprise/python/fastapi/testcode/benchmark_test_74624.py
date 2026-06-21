# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db


async def BenchmarkTest74624(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data, _sep, _rest = str(db_value).partition('\x00')
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
