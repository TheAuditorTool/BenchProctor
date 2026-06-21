# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest23327(request: Request):
    auth_header = request.headers.get('authorization', '')
    if auth_header:
        data = auth_header
    else:
        data = ''
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return {"updated": True}
