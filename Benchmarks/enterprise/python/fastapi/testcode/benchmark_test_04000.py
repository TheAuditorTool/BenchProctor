# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest04000(request: Request):
    auth_header = request.headers.get('authorization', '')
    size = min(int(auth_header) if str(auth_header).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
