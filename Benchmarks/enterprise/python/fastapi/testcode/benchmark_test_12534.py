# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time
from app_runtime import db


request_state: dict[str, str] = {}

async def BenchmarkTest12534(request: Request):
    host_value = request.headers.get('host', '')
    request_state['last_input'] = host_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return {"updated": True}
