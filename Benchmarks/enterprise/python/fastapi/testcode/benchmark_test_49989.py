# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest49989(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = f'{header_value}'
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
