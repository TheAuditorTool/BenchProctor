# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest15669(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = ua_value if ua_value else 'default'
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return {"updated": True}
