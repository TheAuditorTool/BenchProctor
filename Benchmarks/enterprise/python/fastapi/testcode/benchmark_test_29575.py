# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


request_state: dict[str, str] = {}

async def BenchmarkTest29575(request: Request):
    upload_name = (await request.form()).get('upload', '')
    request_state['last_input'] = upload_name
    data = request_state['last_input']
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
