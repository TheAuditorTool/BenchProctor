# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest45002(request: Request):
    host_value = request.headers.get('host', '')
    if host_value:
        data = host_value
    else:
        data = ''
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
