# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest12441(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    parts = []
    for token in str(header_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    os.seteuid(65534)
    return {"updated": True}
