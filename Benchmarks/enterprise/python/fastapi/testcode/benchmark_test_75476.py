# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest75476(request: Request):
    host_value = request.headers.get('host', '')
    parts = []
    for token in str(host_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    int(str(data))
    return {"updated": True}
