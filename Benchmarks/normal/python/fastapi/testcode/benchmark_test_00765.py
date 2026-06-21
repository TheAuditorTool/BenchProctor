# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest00765(request: Request):
    origin_value = request.headers.get('origin', '')
    data = (lambda v: v.strip())(origin_value)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
