# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest05766(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    ctx = RequestContext(forwarded_ip)
    data = ctx.payload
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(digest)
    return {"updated": True}
