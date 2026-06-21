# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest12752(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = auth_header if auth_header else 'default'
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
