# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest07085(request: Request):
    host_value = request.headers.get('host', '')
    data = f'{host_value:.200s}'
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return {"updated": True}
