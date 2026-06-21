# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from fastapi import Form
from app_runtime import auth_check


request_state: dict[str, str] = {}

async def BenchmarkTest06499(request: Request, field: str = Form('')):
    field_value = field
    request_state['last_input'] = field_value
    data = request_state['last_input']
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return {"updated": True}
