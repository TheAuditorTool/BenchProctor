# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


request_state: dict[str, str] = {}

async def BenchmarkTest38067(request: Request, field: str = Form('')):
    field_value = field
    request_state['last_input'] = field_value
    data = request_state['last_input']
    async def _evasion_task():
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return content
    return await _evasion_task()
