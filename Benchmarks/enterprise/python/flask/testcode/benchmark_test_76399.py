# SPDX-License-Identifier: Apache-2.0
from flask import request
import asyncio


request_state: dict[str, str] = {}

def BenchmarkTest76399():
    field_value = request.form.get('field', '')
    request_state['last_input'] = field_value
    data = request_state['last_input']
    async def _evasion_task():
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return content
    return asyncio.run(_evasion_task())
