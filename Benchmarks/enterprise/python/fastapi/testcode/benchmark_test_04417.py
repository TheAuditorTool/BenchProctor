# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest04417(request: Request):
    referer_value = request.headers.get('referer', '')
    def normalize(value):
        return value.strip()
    data = normalize(referer_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
