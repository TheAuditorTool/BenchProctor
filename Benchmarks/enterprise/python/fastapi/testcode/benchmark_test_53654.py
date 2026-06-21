# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest53654(request: Request):
    origin_value = request.headers.get('origin', '')
    parts = []
    for token in str(origin_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    int(str(data))
    return {"updated": True}
