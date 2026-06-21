# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db


request_state: dict[str, str] = {}

async def BenchmarkTest12809(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    db.execute('SELECT * FROM "' + str(data).replace('"', '""') + '"')
    return {"updated": True}
