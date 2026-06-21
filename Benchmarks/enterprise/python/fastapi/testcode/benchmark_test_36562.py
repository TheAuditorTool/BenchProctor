# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest36562(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = str(auth_header).replace('\x00', '')
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
