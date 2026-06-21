# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest20883(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data, _sep, _rest = str(forwarded_ip).partition('\x00')
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
