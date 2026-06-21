# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest28615(request: Request):
    ua_value = request.headers.get('user-agent', '')
    if ua_value:
        data = ua_value
    else:
        data = ''
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
