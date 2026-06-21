# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile


request_state: dict[str, str] = {}

async def BenchmarkTest81166(request: Request):
    auth_header = request.headers.get('authorization', '')
    request_state['last_input'] = auth_header
    data = request_state['last_input']
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
