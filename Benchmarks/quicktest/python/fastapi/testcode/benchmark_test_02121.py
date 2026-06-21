# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest02121(request: Request):
    auth_header = request.headers.get('authorization', '')
    if auth_header:
        data = auth_header
    else:
        data = ''
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
