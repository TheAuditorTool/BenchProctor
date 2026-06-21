# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest14229(request: Request):
    origin_value = request.headers.get('origin', '')
    size = min(int(origin_value) if str(origin_value).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
