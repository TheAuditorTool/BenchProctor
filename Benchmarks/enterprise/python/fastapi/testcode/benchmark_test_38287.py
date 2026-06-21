# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest38287(request: Request):
    host_value = request.headers.get('host', '')
    if host_value:
        data = host_value
    else:
        data = ''
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
