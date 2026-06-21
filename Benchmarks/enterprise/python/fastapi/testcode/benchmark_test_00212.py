# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest00212(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = f'{auth_header}'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
