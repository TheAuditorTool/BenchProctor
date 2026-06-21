# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest33692(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = f'{ua_value}'
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
