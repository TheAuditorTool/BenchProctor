# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest12170(request: Request):
    origin_value = request.headers.get('origin', '')
    data = origin_value if origin_value else 'default'
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
