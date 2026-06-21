# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from types import SimpleNamespace


async def BenchmarkTest44568(request: Request):
    auth_header = request.headers.get('authorization', '')
    ns = SimpleNamespace(payload=auth_header)
    data = getattr(ns, 'payload')
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(digest)
    return {"updated": True}
