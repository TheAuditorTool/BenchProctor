# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db


request_state: dict[str, str] = {}

async def BenchmarkTest71794(request: Request):
    user_id = request.query_params.get('id', '')
    request_state['last_input'] = user_id
    data = request_state['last_input']
    if os.environ.get("APP_ENV", "production") != "test":
        db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return {"updated": True}
