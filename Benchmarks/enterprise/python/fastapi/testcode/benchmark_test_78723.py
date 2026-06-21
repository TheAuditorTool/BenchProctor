# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


request_state: dict[str, str] = {}

async def BenchmarkTest78723(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    request_state['last_input'] = forwarded_ip
    data = request_state['last_input']
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return {"updated": True}
