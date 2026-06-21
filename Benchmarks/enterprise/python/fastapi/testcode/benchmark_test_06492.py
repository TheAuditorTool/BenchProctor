# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest06492(request: Request):
    host_value = request.headers.get('host', '')
    data = ' '.join(str(host_value).split())
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return {"updated": True}
