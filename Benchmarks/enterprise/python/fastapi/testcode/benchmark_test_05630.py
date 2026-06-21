# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest05630(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = bytes.fromhex(cookie_value).decode('utf-8', 'ignore')
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
