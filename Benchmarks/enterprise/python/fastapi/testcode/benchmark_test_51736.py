# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


request_state: dict[str, str] = {}

async def BenchmarkTest51736(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    request_state['last_input'] = raw_body
    data = request_state['last_input']
    async def _evasion_task():
        with open('/var/uploads/' + str(data), 'wb') as fh:
            fh.write(b'data')
    await _evasion_task()
    return {"updated": True}
