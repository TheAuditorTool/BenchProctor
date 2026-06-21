# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest49495(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = ua_value if ua_value else 'default'
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
