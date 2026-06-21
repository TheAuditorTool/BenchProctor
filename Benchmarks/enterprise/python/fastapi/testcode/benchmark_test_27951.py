# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest27951(request: Request):
    origin_value = request.headers.get('origin', '')
    if origin_value:
        data = origin_value
    else:
        data = ''
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
