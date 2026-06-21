# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from app_runtime import db


request_state: dict[str, str] = {}

async def BenchmarkTest59662(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    request_state['last_input'] = raw_body
    data = request_state['last_input']
    async def _evasion_task():
        _resp = requests.get(str(data))
        db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    await _evasion_task()
    return {"updated": True}
