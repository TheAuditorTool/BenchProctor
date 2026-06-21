# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


request_state: dict[str, str] = {}

async def BenchmarkTest28427(request: Request):
    user_id = request.query_params.get('id', '')
    request_state['last_input'] = user_id
    data = request_state['last_input']
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
