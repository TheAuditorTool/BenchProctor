# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time
from app_runtime import db


async def BenchmarkTest35707(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(db_value)
    return {"updated": True}
