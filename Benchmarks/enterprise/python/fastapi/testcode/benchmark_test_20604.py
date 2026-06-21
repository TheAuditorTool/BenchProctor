# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


request_state: dict[str, str] = {}

async def BenchmarkTest20604(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    request_state['last_input'] = forwarded_ip
    data = request_state['last_input']
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
