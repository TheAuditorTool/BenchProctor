# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib
import sys


request_state: dict[str, str] = {}

async def BenchmarkTest59356(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    request_state['last_input'] = header_value
    data = request_state['last_input']
    def _primary():
        sys.path.insert(0, str(data))
        importlib.import_module('report_renderer')
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
