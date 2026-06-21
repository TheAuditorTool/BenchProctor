# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest11107(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    checked_path = os.path.join('/var/app/data', os.path.basename(forwarded_ip))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
