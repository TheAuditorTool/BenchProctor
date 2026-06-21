# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest69110(request: Request):
    host_value = request.headers.get('host', '')
    data = '%s' % (host_value,)
    eval(str(data))
    return {"updated": True}
