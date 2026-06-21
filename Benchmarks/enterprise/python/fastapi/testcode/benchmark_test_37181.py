# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest37181(request: Request):
    auth_header = request.headers.get('authorization', '')
    data, _sep, _rest = str(auth_header).partition('\x00')
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
