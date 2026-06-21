# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest13209(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(forwarded_ip)
    data = collected
    os.remove(str(data))
    return {"updated": True}
