# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest06563(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(db_value))
    return {"updated": True}
