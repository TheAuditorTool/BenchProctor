# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest24811(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = ua_value if ua_value else 'default'
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
