# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest31312(request: Request):
    auth_header = request.headers.get('authorization', '')
    data, _sep, _rest = str(auth_header).partition('\x00')
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
