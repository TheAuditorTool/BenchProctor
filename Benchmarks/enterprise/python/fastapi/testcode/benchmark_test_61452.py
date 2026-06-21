# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


request_state: dict[str, str] = {}

async def BenchmarkTest61452(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    request_state['last_input'] = raw_body
    data = request_state['last_input']
    result = 100 / int(str(data))
    return {"updated": True}
