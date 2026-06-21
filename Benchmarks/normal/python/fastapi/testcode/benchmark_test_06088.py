# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest06088(request: Request):
    host_value = request.headers.get('host', '')
    data = '%s' % (host_value,)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
