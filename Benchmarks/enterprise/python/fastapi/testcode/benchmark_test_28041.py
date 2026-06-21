# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest28041(request: Request):
    referer_value = request.headers.get('referer', '')
    if referer_value:
        data = referer_value
    else:
        data = ''
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
