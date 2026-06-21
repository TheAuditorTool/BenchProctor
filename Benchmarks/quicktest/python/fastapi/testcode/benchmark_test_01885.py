# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest01885(request: Request):
    host_value = request.headers.get('host', '')
    parts = str(host_value).split(',')
    data = ','.join(parts)
    eval(str(data))
    return {"updated": True}
