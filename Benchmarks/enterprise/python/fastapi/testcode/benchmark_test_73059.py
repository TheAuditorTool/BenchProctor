# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest73059(request: Request):
    origin_value = request.headers.get('origin', '')
    data = origin_value if origin_value else 'default'
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
