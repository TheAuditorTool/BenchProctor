# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import runpy


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest06895(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    ctx = RequestContext(header_value)
    data = ctx.payload
    def _primary():
        with open('plugins/generated_config.py', 'w') as fh:
            fh.write('SETTING = "' + str(data) + '"')
        runpy.run_path('plugins/generated_config.py')
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
