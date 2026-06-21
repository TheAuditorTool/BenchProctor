# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest10682(request: Request):
    origin_value = request.headers.get('origin', '')
    parts = str(origin_value).split(',')
    data = ','.join(parts)
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
