# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest56303(request: Request):
    host_value = request.headers.get('host', '')
    if host_value:
        data = host_value
    else:
        data = ''
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        pass
    return {"updated": True}
