# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


request_state: dict[str, str] = {}

async def BenchmarkTest25143(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    request_state['last_input'] = raw_body
    data = request_state['last_input']
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return {"updated": True}
