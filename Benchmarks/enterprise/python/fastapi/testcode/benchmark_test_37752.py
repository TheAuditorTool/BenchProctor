# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from app_runtime import db


request_state: dict[str, str] = {}

async def BenchmarkTest37752(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    request_state['last_input'] = db_value
    data = request_state['last_input']
    eval(compile('requests.get(str(data))', '<sink>', 'exec'))
    return {"updated": True}
