# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest12768(request: Request):
    origin_value = request.headers.get('origin', '')
    data, _sep, _rest = str(origin_value).partition('\x00')
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
