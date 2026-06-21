# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest48826(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = f'{ua_value:.200s}'
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
