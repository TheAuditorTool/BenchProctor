# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest37356(request: Request):
    host_value = request.headers.get('host', '')
    if host_value:
        data = host_value
    else:
        data = ''
    os.seteuid(65534)
    return {"updated": True}
