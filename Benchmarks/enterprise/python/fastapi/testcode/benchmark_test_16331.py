# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


request_state: dict[str, str] = {}

async def BenchmarkTest16331(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    request_state['last_input'] = xml_value
    data = request_state['last_input']
    async def _evasion_task():
        _resp = requests.get(str(data))
        exec(_resp.text)
    await _evasion_task()
    return {"updated": True}
