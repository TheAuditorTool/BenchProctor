# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import pickle


request_state: dict[str, str] = {}

async def BenchmarkTest16634(request: Request):
    auth_header = request.headers.get('authorization', '')
    request_state['last_input'] = auth_header
    data = request_state['last_input']
    async def _evasion_task():
        pickle.loads(data.encode('latin-1'))
    await _evasion_task()
    return {"updated": True}
