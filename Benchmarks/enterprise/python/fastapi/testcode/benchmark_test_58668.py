# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest58668(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    pending = list(str(cookie_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
