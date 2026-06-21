# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest72431(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = auth_header if auth_header else 'default'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
