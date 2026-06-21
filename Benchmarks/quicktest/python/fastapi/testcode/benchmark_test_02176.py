# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest02176(request: Request):
    origin_value = request.headers.get('origin', '')
    data = origin_value if origin_value else 'default'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
