# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest09062(request: Request):
    host_value = request.headers.get('host', '')
    globals().setdefault('_secret_cache', {})['current'] = str(host_value)
    return {"updated": True}
