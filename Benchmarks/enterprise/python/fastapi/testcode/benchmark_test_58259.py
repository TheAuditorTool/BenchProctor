# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile


request_state: dict[str, str] = {}

async def BenchmarkTest58259(request: Request):
    user_id = request.query_params.get('id', '')
    request_state['last_input'] = user_id
    data = request_state['last_input']
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
