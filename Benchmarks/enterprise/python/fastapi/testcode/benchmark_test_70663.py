# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest70663(request: Request):
    origin_value = request.headers.get('origin', '')
    parts = str(origin_value).split(',')
    data = ','.join(parts)
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
