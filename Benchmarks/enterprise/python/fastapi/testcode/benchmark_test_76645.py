# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest76645(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    prefix = ''
    data = prefix + str(header_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
