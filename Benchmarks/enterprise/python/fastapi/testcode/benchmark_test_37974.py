# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest37974(request: Request):
    origin_value = request.headers.get('origin', '')
    parts = str(origin_value).split(',')
    data = ','.join(parts)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
