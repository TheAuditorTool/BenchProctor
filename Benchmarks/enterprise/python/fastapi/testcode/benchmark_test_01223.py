# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest01223(request: Request):
    origin_value = request.headers.get('origin', '')
    link_path = os.path.join('/var/app/data', str(origin_value))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
