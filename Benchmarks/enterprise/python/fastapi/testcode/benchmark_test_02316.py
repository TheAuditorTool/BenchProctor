# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest02316(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = f'{forwarded_ip:.200s}'
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
