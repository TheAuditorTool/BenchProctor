# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


request_state: dict[str, str] = {}

async def BenchmarkTest01574(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    request_state['last_input'] = raw_body
    data = request_state['last_input']
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return {"updated": True}
