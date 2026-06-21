# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


async def BenchmarkTest22140(request: Request):
    origin_value = request.headers.get('origin', '')
    parts = []
    for token in str(origin_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    globals()['counter'] = int(data)
    return {"updated": True}
