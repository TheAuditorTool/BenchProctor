# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest54210(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = f'{auth_header}'
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
