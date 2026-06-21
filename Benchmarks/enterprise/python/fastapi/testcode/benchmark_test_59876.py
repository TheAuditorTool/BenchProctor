# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest59876(request: Request):
    host_value = request.headers.get('host', '')
    prefix = ''
    data = prefix + str(host_value)
    int(str(data))
    return {"updated": True}
