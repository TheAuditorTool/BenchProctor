# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest15618(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    if header_value:
        data = header_value
    else:
        data = ''
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
