# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest03367(request: Request):
    auth_header = request.headers.get('authorization', '')
    data, _sep, _rest = str(auth_header).partition('\x00')
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
