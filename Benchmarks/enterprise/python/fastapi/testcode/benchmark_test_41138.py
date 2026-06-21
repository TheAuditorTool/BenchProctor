# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest41138(request: Request):
    auth_header = request.headers.get('authorization', '')
    prefix = ''
    data = prefix + str(auth_header)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
