# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest27980(request: Request):
    ua_value = request.headers.get('user-agent', '')
    parts = []
    for token in str(ua_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    os.remove(str(data))
    return {"updated": True}
