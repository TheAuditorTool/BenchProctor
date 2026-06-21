# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time
from app_runtime import db


async def BenchmarkTest42784(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = db_value if db_value else 'default'
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
