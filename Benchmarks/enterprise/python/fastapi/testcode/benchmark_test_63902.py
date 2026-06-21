# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time
from app_runtime import db


def to_text(value):
    return str(value).strip()

async def BenchmarkTest63902(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = to_text(db_value)
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
