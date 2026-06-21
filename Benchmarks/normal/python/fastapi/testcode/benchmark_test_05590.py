# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


request_state: dict[str, str] = {}

async def BenchmarkTest05590(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    request_state['last_input'] = cookie_value
    data = request_state['last_input']
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
