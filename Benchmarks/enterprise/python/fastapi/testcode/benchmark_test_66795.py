# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest66795(request: Request):
    referer_value = request.headers.get('referer', '')
    prefix = ''
    data = prefix + str(referer_value)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
