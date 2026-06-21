# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest55050(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = forwarded_ip if forwarded_ip else 'default'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
