# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest27327(request: Request):
    host_value = request.headers.get('host', '')
    data = (lambda v: v.strip())(host_value)
    int(str(data))
    return {"updated": True}
