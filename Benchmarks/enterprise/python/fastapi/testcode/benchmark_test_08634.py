# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


async def BenchmarkTest08634(request: Request):
    host_value = request.headers.get('host', '')
    parts = []
    for token in str(host_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    globals()['counter'] = int(data)
    return {"updated": True}
