# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


request_state: dict[str, str] = {}

async def BenchmarkTest76050(request: Request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    request_state['last_input'] = profile_value
    data = request_state['last_input']
    processed = data[:64]
    with open('/var/app/data/' + str(processed), 'w') as fh:
        fh.write('data')
    return {"updated": True}
