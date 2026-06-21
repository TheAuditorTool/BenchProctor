# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest29082(request: Request):
    referer_value = request.headers.get('referer', '')
    data = ' '.join(str(referer_value).split())
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
