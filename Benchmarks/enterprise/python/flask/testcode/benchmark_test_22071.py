# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request
import asyncio


request_state: dict[str, str] = {}

def BenchmarkTest22071():
    header_value = request.headers.get('X-Custom-Header', '')
    request_state['last_input'] = header_value
    data = request_state['last_input']
    async def _evasion_task():
        return render_template_string(data)
    return asyncio.run(_evasion_task())
