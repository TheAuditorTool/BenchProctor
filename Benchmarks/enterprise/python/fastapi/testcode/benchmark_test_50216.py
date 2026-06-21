# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest50216(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    parts = []
    for token in str(forwarded_ip).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
