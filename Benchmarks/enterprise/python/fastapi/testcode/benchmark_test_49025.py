# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


request_state: dict[str, str] = {}

async def BenchmarkTest49025(request: Request):
    upload_name = (await request.form()).get('upload', '')
    request_state['last_input'] = upload_name
    data = request_state['last_input']
    auth_check('user', data)
    return {"updated": True}
