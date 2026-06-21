# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest02589(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = (lambda v: v.strip())(forwarded_ip)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
