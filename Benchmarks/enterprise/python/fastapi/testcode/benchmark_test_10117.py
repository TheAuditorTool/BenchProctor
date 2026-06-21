# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest10117(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = str(forwarded_ip).replace('\x00', '')
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
