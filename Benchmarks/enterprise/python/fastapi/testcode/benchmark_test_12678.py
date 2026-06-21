# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import runpy


request_state: dict[str, str] = {}

async def BenchmarkTest12678(request: Request):
    origin_value = request.headers.get('origin', '')
    request_state['last_input'] = origin_value
    data = request_state['last_input']
    async def _evasion_task():
        with open('plugins/generated_config.py', 'w') as fh:
            fh.write('SETTING = "' + str(data) + '"')
        runpy.run_path('plugins/generated_config.py')
    await _evasion_task()
    return {"updated": True}
