# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest76109(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = f'{auth_header:.200s}'
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
