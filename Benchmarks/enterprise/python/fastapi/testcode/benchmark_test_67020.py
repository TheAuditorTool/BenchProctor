# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


request_state: dict[str, str] = {}

async def BenchmarkTest67020(request: Request):
    auth_header = request.headers.get('authorization', '')
    request_state['last_input'] = auth_header
    data = request_state['last_input']
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
