# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest68184(request: Request):
    host_value = request.headers.get('host', '')
    data = '%s' % (host_value,)
    result = 100 / int(str(data))
    return {"updated": True}
