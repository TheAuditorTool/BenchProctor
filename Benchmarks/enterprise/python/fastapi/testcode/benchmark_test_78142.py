# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest78142(request: Request):
    auth_header = request.headers.get('authorization', '')
    link_path = os.path.join('/var/app/data', str(auth_header))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
