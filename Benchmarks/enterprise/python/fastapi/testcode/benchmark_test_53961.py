# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def ensure_str(value):
    return str(value)

async def BenchmarkTest53961(request: Request):
    referer_value = request.headers.get('referer', '')
    data = ensure_str(referer_value)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
