# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest76348(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data, _sep, _rest = str(ua_value).partition('\x00')
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return {"updated": True}
