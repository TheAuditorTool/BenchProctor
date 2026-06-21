# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest67179(request: Request):
    referer_value = request.headers.get('referer', '')
    prefix = ''
    data = prefix + str(referer_value)
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
