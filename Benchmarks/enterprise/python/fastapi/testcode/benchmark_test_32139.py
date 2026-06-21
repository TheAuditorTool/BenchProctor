# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest32139(request: Request):
    auth_header = request.headers.get('authorization', '')
    if auth_header:
        data = auth_header
    else:
        data = ''
    eval(str(data))
    return {"updated": True}
