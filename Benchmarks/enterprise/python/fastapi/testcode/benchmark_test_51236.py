# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


request_state: dict[str, str] = {}

async def BenchmarkTest51236(request: Request):
    auth_header = request.headers.get('authorization', '')
    request_state['last_input'] = auth_header
    data = request_state['last_input']
    async def _evasion_task():
        with open('/var/www/html/exports/report.txt', 'w') as fh:
            fh.write(str(data))
    await _evasion_task()
    return {"updated": True}
