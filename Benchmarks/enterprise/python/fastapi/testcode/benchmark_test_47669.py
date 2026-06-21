# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest47669(request: Request):
    host_value = request.headers.get('host', '')
    data, _sep, _rest = str(host_value).partition('\x00')
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
