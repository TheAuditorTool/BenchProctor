# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest62302(request: Request):
    host_value = request.headers.get('host', '')
    data = (lambda v: v.strip())(host_value)
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
