# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import base64
import time
from app_runtime import db


async def BenchmarkTest45666(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
