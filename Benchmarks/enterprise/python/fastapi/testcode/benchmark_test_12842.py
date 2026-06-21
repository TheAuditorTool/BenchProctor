# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest12842(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    if header_value:
        data = header_value
    else:
        data = ''
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
