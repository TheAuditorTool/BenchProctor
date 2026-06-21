# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest67603(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value}'
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
