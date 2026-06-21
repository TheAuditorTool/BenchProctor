# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest35410(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data, _sep, _rest = str(header_value).partition('\x00')
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
