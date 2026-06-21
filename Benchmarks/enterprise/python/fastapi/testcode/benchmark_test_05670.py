# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest05670(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = ' '.join(str(auth_header).split())
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
