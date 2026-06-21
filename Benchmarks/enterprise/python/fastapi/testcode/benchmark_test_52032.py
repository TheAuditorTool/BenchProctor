# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest52032(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(forwarded_ip)
    data = collected
    processed = data[:64]
    exec(str(processed))
    return {"updated": True}
