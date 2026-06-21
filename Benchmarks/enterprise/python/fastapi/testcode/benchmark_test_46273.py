# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest46273(request: Request):
    host_value = request.headers.get('host', '')
    data = f'{host_value:.200s}'
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
