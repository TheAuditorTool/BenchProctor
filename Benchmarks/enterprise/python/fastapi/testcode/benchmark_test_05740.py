# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest05740(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = ' '.join(str(header_value).split())
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
