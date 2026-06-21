# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest03064(request: Request):
    origin_value = request.headers.get('origin', '')
    data = (lambda v: v.strip())(origin_value)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
