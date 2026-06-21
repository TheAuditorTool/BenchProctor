# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest52771(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = auth_header if auth_header else 'default'
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
