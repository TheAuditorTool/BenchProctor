# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest36657(request: Request):
    host_value = request.headers.get('host', '')
    parts = []
    for token in str(host_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    os.remove(str(data))
    return {"updated": True}
