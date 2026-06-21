# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from app_runtime import db


async def BenchmarkTest77371(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = str(db_value).replace('\x00', '')
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(digest)
    return {"updated": True}
