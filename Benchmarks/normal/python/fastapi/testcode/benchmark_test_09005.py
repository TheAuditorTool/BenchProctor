# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest09005(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    link_path = os.path.join('/var/app/data', str(header_value))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
