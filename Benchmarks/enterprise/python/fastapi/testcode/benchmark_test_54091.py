# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest54091(request: Request):
    referer_value = request.headers.get('referer', '')
    prefix = ''
    data = prefix + str(referer_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
