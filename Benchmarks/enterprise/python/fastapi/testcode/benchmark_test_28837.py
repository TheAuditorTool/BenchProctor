# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest28837(request: Request):
    host_value = request.headers.get('host', '')
    prefix = ''
    data = prefix + str(host_value)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
