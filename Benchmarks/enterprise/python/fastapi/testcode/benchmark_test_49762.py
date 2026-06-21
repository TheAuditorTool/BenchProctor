# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest49762(request: Request):
    auth_header = request.headers.get('authorization', '')
    prefix = ''
    data = prefix + str(auth_header)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
