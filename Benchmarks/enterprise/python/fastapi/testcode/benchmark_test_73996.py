# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest73996(request: Request):
    host_value = request.headers.get('host', '')
    parts = str(host_value).split(',')
    data = ','.join(parts)
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
