# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest08427(request: Request):
    host_value = request.headers.get('host', '')
    data = '%s' % str(host_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
