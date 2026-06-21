# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest01773(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = (lambda v: v.strip())(ua_value)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
