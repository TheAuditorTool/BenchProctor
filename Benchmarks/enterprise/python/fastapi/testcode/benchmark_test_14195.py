# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest14195(request: Request):
    host_value = request.headers.get('host', '')
    data = '%s' % str(host_value)
    int(str(data))
    return {"updated": True}
