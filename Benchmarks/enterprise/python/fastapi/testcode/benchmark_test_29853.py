# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest29853(request: Request):
    referer_value = request.headers.get('referer', '')
    data = referer_value if referer_value else 'default'
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
