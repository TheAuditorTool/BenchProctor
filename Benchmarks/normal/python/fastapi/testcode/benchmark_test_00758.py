# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest00758(request: Request):
    auth_header = request.headers.get('authorization', '')
    with open('/var/app/data/' + str(auth_header), 'r') as fh:
        content = fh.read()
    return content
