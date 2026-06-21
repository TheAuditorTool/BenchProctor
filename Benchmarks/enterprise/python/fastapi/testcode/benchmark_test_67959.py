# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest67959(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    parts = str(header_value).split(',')
    data = ','.join(parts)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
