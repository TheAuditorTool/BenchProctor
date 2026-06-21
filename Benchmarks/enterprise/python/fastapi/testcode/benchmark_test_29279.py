# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest29279(request: Request):
    host_value = request.headers.get('host', '')
    with open('/var/app/data/' + str(host_value), 'r') as fh:
        content = fh.read()
    return content
