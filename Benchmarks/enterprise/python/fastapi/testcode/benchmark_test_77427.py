# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest77427(request: Request):
    host_value = request.headers.get('host', '')
    data = '%s' % str(host_value)
    os.remove(str(data))
    return {"updated": True}
