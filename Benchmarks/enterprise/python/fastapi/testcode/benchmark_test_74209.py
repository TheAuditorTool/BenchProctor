# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest74209(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    if raw_body:
        data = raw_body
    else:
        data = ''
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
