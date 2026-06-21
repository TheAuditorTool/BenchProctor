# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest02719(request: Request):
    host_value = request.headers.get('host', '')
    data = '%s' % (host_value,)
    os.remove(str(data))
    return {"updated": True}
