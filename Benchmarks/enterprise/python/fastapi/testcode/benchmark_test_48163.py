# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import importlib


request_state: dict[str, str] = {}

async def BenchmarkTest48163(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    async def _evasion_task():
        importlib.import_module(str(data))
    await _evasion_task()
    return {"updated": True}
