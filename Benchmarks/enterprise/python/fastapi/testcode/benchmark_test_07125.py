# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest07125(request: Request):
    host_value = request.headers.get('host', '')
    with open(os.path.join('/var/app/data', str(host_value)), 'r') as fh:
        content = fh.read()
    return content
