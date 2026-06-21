# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest60265(request: Request):
    auth_header = request.headers.get('authorization', '')
    prefix = ''
    data = prefix + str(auth_header)
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
