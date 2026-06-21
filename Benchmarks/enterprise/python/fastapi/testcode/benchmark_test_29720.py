# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


request_state: dict[str, str] = {}

async def BenchmarkTest29720(request: Request):
    upload_name = (await request.form()).get('upload', '')
    request_state['last_input'] = upload_name
    data = request_state['last_input']
    def _primary():
        os.system('echo ' + str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
