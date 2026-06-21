# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest10548(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    with open('/var/app/data/' + str(header_value), 'r') as fh:
        content = fh.read()
    return content
