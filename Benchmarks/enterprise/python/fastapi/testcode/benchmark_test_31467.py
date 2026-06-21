# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest31467(request: Request):
    origin_value = request.headers.get('origin', '')
    prefix = ''
    data = prefix + str(origin_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
