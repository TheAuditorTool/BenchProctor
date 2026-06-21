# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request
import asyncio


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest46654():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    ctx = RequestContext(json_value)
    data = ctx.payload
    async def _evasion_task():
        return render_template_string(data)
    return asyncio.run(_evasion_task())
