# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest03866(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    with open('/var/app/data/' + str(forwarded_ip), 'r') as fh:
        content = fh.read()
    return content
