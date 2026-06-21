# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest64788(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(header_value)
    data = collected
    int(str(data))
    return {"updated": True}
