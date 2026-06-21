# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest07986(request: Request):
    referer_value = request.headers.get('referer', '')
    prefix = ''
    data = prefix + str(referer_value)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
