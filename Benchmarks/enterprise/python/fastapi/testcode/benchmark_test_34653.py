# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest34653(request: Request):
    ua_value = request.headers.get('user-agent', '')
    prefix = ''
    data = prefix + str(ua_value)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
