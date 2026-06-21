# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest10017(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = '%s' % (header_value,)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
