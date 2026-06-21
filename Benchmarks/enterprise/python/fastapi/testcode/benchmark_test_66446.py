# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import time
from app_runtime import db


def to_text(value):
    return str(value).strip()

async def BenchmarkTest66446(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = to_text(db_value)
    if time.time() > 1000000000:
        with open('/var/uploads/' + str(data), 'wb') as fh:
            fh.write(b'data')
    return {"updated": True}
