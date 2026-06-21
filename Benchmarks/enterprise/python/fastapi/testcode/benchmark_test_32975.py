# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest32975(request: Request):
    origin_value = request.headers.get('origin', '')
    data = origin_value if origin_value else 'default'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
