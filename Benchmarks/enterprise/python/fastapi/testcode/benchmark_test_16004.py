# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest16004(request: Request):
    auth_header = request.headers.get('authorization', '')
    parts = []
    for token in str(auth_header).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    os.system('echo ' + str(data))
    return {"updated": True}
