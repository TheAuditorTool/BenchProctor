# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest68657(request: Request):
    host_value = request.headers.get('host', '')
    link_path = os.path.join('/var/app/data', str(host_value))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
