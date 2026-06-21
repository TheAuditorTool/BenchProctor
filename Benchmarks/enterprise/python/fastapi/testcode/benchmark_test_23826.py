# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import time
from app_runtime import db


request_state: dict[str, str] = {}

async def BenchmarkTest23826(request: Request, field: str = Form('')):
    field_value = field
    request_state['last_input'] = field_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return {"updated": True}
