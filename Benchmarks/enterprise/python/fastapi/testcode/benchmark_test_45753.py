# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from types import SimpleNamespace


async def BenchmarkTest45753(request: Request):
    ua_value = request.headers.get('user-agent', '')
    ns = SimpleNamespace(payload=ua_value)
    data = getattr(ns, 'payload')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
