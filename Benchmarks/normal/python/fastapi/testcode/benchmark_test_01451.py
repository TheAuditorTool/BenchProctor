# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest01451(request: Request):
    host_value = request.headers.get('host', '')
    data = ' '.join(str(host_value).split())
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
