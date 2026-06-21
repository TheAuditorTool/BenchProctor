# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest72712(request: Request):
    host_value = request.headers.get('host', '')
    data = str(host_value).replace('\x00', '')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
