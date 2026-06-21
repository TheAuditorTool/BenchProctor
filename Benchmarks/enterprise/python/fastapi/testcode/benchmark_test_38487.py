# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest38487(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    prefix = ''
    data = prefix + str(header_value)
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
