# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest33629(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = '{}'.format(auth_header)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return {"updated": True}
