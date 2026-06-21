# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest23025(request: Request):
    host_value = request.headers.get('host', '')
    data = host_value if host_value else 'default'
    os.system('echo ' + str(data))
    return {"updated": True}
