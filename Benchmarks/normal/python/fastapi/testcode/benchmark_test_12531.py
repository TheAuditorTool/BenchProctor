# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest12531(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = header_value if header_value else 'default'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
