# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest49776(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(header_value)
    data = collected
    os.remove(str(data))
    return {"updated": True}
