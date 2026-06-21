# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest09412(request: Request):
    host_value = request.headers.get('host', '')
    if host_value:
        data = host_value
    else:
        data = ''
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
