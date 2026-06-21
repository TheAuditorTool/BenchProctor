# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest05513(request: Request):
    auth_header = request.headers.get('authorization', '')
    prefix = ''
    data = prefix + str(auth_header)
    eval(str(data))
    return {"updated": True}
