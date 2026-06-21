# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest54643(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = str(header_value).replace('\x00', '')
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
