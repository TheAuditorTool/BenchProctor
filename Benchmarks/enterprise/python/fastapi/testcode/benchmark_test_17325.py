# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest17325(request: Request):
    ua_value = request.headers.get('user-agent', '')
    parts = []
    for token in str(ua_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    int(str(data))
    return {"updated": True}
