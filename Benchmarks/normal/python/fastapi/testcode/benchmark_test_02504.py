# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest02504(request: Request):
    origin_value = request.headers.get('origin', '')
    data = f'{origin_value}'
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
