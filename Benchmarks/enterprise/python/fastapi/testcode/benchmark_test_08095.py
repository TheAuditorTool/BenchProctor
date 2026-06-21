# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest08095(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = header_value if header_value else 'default'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
