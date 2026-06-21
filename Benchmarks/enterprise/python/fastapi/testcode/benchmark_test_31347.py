# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest31347(request: Request):
    host_value = request.headers.get('host', '')
    result = 100 / int(str(host_value))
    return {"updated": True}
