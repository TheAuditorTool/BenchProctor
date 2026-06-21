# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest74469(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = (lambda v: v.strip())(auth_header)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
