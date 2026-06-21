# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest35025(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = '%s' % str(header_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
