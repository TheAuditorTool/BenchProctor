# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest45610(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = (lambda v: v.strip())(ua_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
