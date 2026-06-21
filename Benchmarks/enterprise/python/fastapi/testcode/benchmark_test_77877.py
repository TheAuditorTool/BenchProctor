# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest77877(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    parts = []
    for token in str(header_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
