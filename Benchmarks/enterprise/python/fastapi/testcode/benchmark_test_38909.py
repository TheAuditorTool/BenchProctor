# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time
from app_runtime import db


async def BenchmarkTest38909(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    prefix = ''
    data = prefix + str(db_value)
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
