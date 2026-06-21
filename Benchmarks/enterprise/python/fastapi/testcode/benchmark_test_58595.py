# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest58595(request: Request):
    host_value = request.headers.get('host', '')
    data = str(host_value).replace('\x00', '')
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
