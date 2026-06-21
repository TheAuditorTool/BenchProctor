# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import auth_check


request_state: dict[str, str] = {}

async def BenchmarkTest55818(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    request_state['last_input'] = raw_body
    data = request_state['last_input']
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return {"updated": True}
