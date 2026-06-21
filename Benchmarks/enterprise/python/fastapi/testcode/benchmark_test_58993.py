# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest58993(request: Request):
    host_value = request.headers.get('host', '')
    data = host_value if host_value else 'default'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
