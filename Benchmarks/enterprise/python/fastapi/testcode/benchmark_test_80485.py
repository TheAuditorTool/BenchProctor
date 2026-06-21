# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db


request_state: dict[str, str] = {}

async def BenchmarkTest80485(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    request_state['last_input'] = db_value
    data = request_state['last_input']
    if os.environ.get("APP_ENV", "production") != "test":
        eval(str(data))
    return {"updated": True}
