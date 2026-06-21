# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


async def BenchmarkTest01785(request: Request):
    ua_value = request.headers.get('user-agent', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(ua_value)
    data = collected
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
