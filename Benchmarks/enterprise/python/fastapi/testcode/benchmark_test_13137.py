# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest13137(request: Request):
    auth_header = request.headers.get('authorization', '')
    prefix = ''
    data = prefix + str(auth_header)
    int(str(data))
    return {"updated": True}
