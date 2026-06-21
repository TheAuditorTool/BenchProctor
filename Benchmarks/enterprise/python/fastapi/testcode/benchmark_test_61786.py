# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest61786(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = f'{forwarded_ip:.200s}'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
