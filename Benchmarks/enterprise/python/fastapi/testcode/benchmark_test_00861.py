# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db


request_state: dict[str, str] = {}

async def BenchmarkTest00861(request: Request):
    auth_header = request.headers.get('authorization', '')
    request_state['last_input'] = auth_header
    data = request_state['last_input']
    if os.environ.get("APP_ENV", "production") != "test":
        db.users.find({'$where': "this.username == '" + str(data) + "'"})
    return {"updated": True}
