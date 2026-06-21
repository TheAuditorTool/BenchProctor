# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import base64
import tempfile
from app_runtime import db


async def BenchmarkTest29351(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
