# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest36219(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = '{}'.format(forwarded_ip)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
