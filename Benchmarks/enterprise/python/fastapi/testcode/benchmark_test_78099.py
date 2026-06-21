# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db


def ensure_str(value):
    return str(value)

async def BenchmarkTest78099(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = ensure_str(db_value)
    if os.environ.get("APP_ENV", "production") != "test":
        with open('/var/uploads/' + str(data), 'wb') as fh:
            fh.write(b'data')
    return {"updated": True}
