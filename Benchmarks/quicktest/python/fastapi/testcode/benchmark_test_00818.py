# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


def to_text(value):
    return str(value).strip()

async def BenchmarkTest00818(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = to_text(db_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
