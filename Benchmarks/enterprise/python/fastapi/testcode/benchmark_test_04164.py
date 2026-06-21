# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest04164(request: Request):
    host_value = request.headers.get('host', '')
    data = f'{host_value:.200s}'
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
