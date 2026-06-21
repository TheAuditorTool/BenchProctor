# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


request_state: dict[str, str] = {}

async def BenchmarkTest62561(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    request_state['last_input'] = xml_value
    data = request_state['last_input']
    def _primary():
        return HTMLResponse('<img src="' + str(data) + '">')
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
