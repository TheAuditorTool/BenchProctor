# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest04338(request: Request):
    auth_header = request.headers.get('authorization', '')
    parts = str(auth_header).split(',')
    data = ','.join(parts)
    eval(str(data))
    return {"updated": True}
