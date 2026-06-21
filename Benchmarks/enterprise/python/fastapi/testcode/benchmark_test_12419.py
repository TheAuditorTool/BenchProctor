# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest12419(request: Request):
    origin_value = request.headers.get('origin', '')
    data = str(origin_value).replace('\x00', '')
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
