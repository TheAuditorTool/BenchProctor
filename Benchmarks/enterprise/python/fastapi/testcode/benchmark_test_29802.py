# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


request_state: dict[str, str] = {}

async def BenchmarkTest29802(request: Request):
    host_value = request.headers.get('host', '')
    request_state['last_input'] = host_value
    data = request_state['last_input']
    db.execute('UPDATE users SET role = ? WHERE name = ?', ('admin', str(data)))
    return {"updated": True}
