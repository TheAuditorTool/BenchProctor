# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest01199(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = '%s' % str(auth_header)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
