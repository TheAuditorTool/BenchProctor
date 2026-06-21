# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import tempfile


request_state: dict[str, str] = {}

async def BenchmarkTest08112(request: Request):
    origin_value = request.headers.get('origin', '')
    request_state['last_input'] = origin_value
    data = request_state['last_input']
    checked_path = os.path.normpath(data)
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(checked_path))
    return {"updated": True}
