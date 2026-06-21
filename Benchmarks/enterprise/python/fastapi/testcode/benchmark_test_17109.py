# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


request_state: dict[str, str] = {}

async def BenchmarkTest17109(request: Request):
    ua_value = request.headers.get('user-agent', '')
    request_state['last_input'] = ua_value
    data = request_state['last_input']
    processed = data[:64]
    db.users.find({'$where': "this.username == '" + str(processed) + "'"})
    return {"updated": True}
