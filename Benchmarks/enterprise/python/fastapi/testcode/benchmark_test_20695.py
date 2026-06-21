# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest20695(request: Request):
    host_value = request.headers.get('host', '')
    data = host_value if host_value else 'default'
    result = 100 / int(str(data))
    return {"updated": True}
