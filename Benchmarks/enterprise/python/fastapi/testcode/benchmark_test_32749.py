# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest32749(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = f'{header_value:.200s}'
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
