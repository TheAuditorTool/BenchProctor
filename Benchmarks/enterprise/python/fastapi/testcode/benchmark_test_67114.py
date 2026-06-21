# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import base64
from app_runtime import db


async def BenchmarkTest67114(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
