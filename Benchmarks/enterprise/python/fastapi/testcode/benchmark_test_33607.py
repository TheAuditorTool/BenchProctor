# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest33607(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = bytes.fromhex(auth_header).decode('utf-8', 'ignore')
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
