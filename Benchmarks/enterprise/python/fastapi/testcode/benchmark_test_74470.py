# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest74470(request: Request):
    ua_value = request.headers.get('user-agent', '')
    def normalize(value):
        return value.strip()
    data = normalize(ua_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
