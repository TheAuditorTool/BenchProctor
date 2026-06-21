# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest17693(request: Request):
    auth_header = request.headers.get('authorization', '')
    data, _sep, _rest = str(auth_header).partition('\x00')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
