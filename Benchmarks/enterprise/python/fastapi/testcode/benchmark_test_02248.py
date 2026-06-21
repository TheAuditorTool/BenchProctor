# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db


request_state: dict[str, str] = {}

async def BenchmarkTest02248(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    request_state['last_input'] = db_value
    data = request_state['last_input']
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return {"updated": True}
