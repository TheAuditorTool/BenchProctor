# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest16822(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data, _sep, _rest = str(ua_value).partition('\x00')
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return {"updated": True}
