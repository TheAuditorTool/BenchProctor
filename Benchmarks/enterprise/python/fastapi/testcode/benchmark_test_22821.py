# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest22821(request: Request):
    host_value = request.headers.get('host', '')
    data = host_value if host_value else 'default'
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return {"updated": True}
