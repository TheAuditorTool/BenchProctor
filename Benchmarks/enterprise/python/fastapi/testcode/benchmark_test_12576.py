# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest12576(request: Request):
    auth_header = request.headers.get('authorization', '')
    parts = []
    for token in str(auth_header).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    eval(str(data))
    return {"updated": True}
