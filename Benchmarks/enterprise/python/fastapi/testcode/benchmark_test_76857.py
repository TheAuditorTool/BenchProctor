# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest76857(request: Request):
    host_value = request.headers.get('host', '')
    data = host_value if host_value else 'default'
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
