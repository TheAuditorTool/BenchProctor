# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest39394(request: Request):
    referer_value = request.headers.get('referer', '')
    parts = str(referer_value).split(',')
    data = ','.join(parts)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
