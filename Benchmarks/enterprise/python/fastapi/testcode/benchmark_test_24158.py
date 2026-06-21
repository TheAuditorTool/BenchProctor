# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest24158(request: Request):
    host_value = request.headers.get('host', '')
    data = (lambda v: v.strip())(host_value)
    eval(str(data))
    return {"updated": True}
