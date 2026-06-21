# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


request_state: dict[str, str] = {}

async def BenchmarkTest02054(request: Request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    request_state['last_input'] = profile_value
    data = request_state['last_input']
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
