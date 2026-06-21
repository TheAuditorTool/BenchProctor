# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest11641(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '{}'.format(origin_value)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
