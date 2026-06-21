# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest05805(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = str(ua_value).replace('\x00', '')
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
