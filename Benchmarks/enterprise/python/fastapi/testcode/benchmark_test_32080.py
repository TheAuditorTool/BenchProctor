# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest32080(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '{}'.format(origin_value)
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
