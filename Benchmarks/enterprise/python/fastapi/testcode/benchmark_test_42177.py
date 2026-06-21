# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time
from app_runtime import db


request_state: dict[str, str] = {}

async def BenchmarkTest42177(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    request_state['last_input'] = comment_value
    data = request_state['last_input']
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
