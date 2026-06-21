# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest28800(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = auth_header if auth_header else 'default'
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return {"updated": True}
