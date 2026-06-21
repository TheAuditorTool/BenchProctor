# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest53510(request: Request):
    auth_header = request.headers.get('authorization', '')
    parts = str(auth_header).split(',')
    data = ','.join(parts)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
