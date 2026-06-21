# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest37653(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = f'{forwarded_ip:.200s}'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
