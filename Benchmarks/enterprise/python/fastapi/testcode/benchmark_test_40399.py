# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest40399(request: Request):
    host_value = request.headers.get('host', '')
    prefix = ''
    data = prefix + str(host_value)
    result = 100 / int(str(data))
    return {"updated": True}
