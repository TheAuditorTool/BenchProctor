# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest57851(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    prefix = ''
    data = prefix + str(forwarded_ip)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
