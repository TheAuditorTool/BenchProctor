# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest07538(request: Request):
    host_value = request.headers.get('host', '')
    prefix = ''
    data = prefix + str(host_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
