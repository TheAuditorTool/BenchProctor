# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest22553(request: Request):
    host_value = request.headers.get('host', '')
    data = f'{host_value:.200s}'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
