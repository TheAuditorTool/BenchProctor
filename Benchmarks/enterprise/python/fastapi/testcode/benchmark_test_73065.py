# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest73065(request: Request):
    referer_value = request.headers.get('referer', '')
    data = f'{referer_value:.200s}'
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
