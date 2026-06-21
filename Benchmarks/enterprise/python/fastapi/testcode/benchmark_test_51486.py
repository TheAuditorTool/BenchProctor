# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest51486(request: Request):
    referer_value = request.headers.get('referer', '')
    def normalize(value):
        return value.strip()
    data = normalize(referer_value)
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
