# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest00802(request: Request):
    origin_value = request.headers.get('origin', '')
    def normalize(value):
        return value.strip()
    data = normalize(origin_value)
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
