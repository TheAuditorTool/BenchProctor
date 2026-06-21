# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest56516(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(forwarded_ip)
    data = collected
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
