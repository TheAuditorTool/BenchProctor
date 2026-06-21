# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest23535(request: Request):
    host_value = request.headers.get('host', '')
    data = '{}'.format(host_value)
    eval(str(data))
    return {"updated": True}
