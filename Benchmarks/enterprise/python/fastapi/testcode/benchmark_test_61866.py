# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest61866(request: Request):
    host_value = request.headers.get('host', '')
    if host_value:
        data = host_value
    else:
        data = ''
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
