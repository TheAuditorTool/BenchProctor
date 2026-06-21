# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest37585(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    parts = str(raw_body).split(',')
    data = ','.join(parts)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
