# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest09199(request: Request):
    host_value = request.headers.get('host', '')
    parts = str(host_value).split(',')
    data = ','.join(parts)
    result = 100 / int(str(data))
    return {"updated": True}
