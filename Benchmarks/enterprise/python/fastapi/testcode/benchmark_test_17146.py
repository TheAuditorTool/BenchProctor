# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile
from app_runtime import db


async def BenchmarkTest17146(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    if db_value:
        data = db_value
    else:
        data = ''
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
