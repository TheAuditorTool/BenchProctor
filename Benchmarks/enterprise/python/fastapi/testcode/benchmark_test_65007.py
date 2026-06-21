# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from app_runtime import db


request_state: dict[str, str] = {}

async def BenchmarkTest65007(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    request_state['last_input'] = db_value
    data = request_state['last_input']
    def _primary():
        requests.get(str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
