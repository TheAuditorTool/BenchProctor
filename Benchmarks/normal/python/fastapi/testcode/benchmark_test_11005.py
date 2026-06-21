# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


async def BenchmarkTest11005(request: Request):
    host_value = request.headers.get('host', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(host_value)
    data = collected
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
