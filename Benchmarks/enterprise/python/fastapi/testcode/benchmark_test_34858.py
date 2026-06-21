# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest34858(request: Request):
    auth_header = request.headers.get('authorization', '')
    parts = str(auth_header).split(',')
    data = ','.join(parts)
    int(str(data))
    return {"updated": True}
