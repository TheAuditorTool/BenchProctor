# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest03100(request: Request):
    referer_value = request.headers.get('referer', '')
    data, _sep, _rest = str(referer_value).partition('\x00')
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
