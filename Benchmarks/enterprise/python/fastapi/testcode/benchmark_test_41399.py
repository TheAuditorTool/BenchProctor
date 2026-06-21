# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest41399(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    parts = []
    for token in str(header_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    os.system('echo ' + str(data))
    return {"updated": True}
