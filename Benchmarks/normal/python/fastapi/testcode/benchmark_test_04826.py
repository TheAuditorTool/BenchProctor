# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


request_state: dict[str, str] = {}

async def BenchmarkTest04826(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    request_state['last_input'] = header_value
    data = request_state['last_input']
    def _primary():
        return HTMLResponse('<div>' + str(data) + '</div>')
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
