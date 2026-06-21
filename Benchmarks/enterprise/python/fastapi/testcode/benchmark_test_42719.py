# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest42719(request: Request):
    auth_header = request.headers.get('authorization', '')
    prefix = ''
    data = prefix + str(auth_header)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return {"updated": True}
