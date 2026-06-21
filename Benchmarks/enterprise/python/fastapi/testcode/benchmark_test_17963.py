# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest17963(request: Request):
    host_value = request.headers.get('host', '')
    if host_value:
        data = host_value
    else:
        data = ''
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return {"updated": True}
