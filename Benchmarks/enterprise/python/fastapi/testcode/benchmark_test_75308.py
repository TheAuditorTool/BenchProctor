# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest75308(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = bytes.fromhex(auth_header).decode('utf-8', 'ignore')
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
