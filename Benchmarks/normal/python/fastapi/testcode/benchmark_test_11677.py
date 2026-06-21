# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest11677(request: Request):
    auth_header = request.headers.get('authorization', '')
    parts = []
    for token in str(auth_header).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return {"updated": True}
