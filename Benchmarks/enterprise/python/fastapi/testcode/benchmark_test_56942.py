# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest56942(request: Request):
    auth_header = request.headers.get('authorization', '')
    parts = str(auth_header).split(',')
    data = ','.join(parts)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
