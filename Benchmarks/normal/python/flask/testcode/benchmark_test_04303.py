# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio


request_state: dict[str, str] = {}

def BenchmarkTest04303():
    auth_header = request.headers.get('Authorization', '')
    request_state['last_input'] = auth_header
    data = request_state['last_input']
    async def _evasion_task():
        with open('/var/www/html/exports/report.txt', 'w') as fh:
            fh.write(str(data))
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
