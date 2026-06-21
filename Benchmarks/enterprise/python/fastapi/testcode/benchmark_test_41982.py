# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest41982(request: Request):
    auth_header = request.headers.get('authorization', '')
    data, _sep, _rest = str(auth_header).partition('\x00')
    result = 100 / int(str(data))
    return {"updated": True}
