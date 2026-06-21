# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest78426(request: Request):
    auth_header = request.headers.get('authorization', '')
    data, _sep, _rest = str(auth_header).partition('\x00')
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return {"updated": True}
