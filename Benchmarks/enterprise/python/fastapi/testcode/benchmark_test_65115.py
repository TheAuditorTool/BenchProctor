# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest65115(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = str(ua_value).replace('\x00', '')
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return {"updated": True}
