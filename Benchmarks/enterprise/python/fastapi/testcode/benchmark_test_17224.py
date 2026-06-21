# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest17224(request: Request):
    host_value = request.headers.get('host', '')
    data = '{}'.format(host_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
