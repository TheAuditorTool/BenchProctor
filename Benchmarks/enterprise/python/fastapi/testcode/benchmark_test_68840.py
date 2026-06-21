# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest68840(request: Request):
    origin_value = request.headers.get('origin', '')
    data = origin_value if origin_value else 'default'
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
