# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest09398(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = f'{ua_value:.200s}'
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return {"updated": True}
