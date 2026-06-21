# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


async def BenchmarkTest10151(request: Request):
    path_value = request.path_params.get('id', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(path_value)
    data = collected
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
