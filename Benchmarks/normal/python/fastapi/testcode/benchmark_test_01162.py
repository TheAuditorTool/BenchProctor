# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile


request_state: dict[str, str] = {}

async def BenchmarkTest01162(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    request_state['last_input'] = raw_body
    data = request_state['last_input']
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
