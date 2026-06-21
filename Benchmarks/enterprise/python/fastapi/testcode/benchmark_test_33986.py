# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest33986(request: Request):
    referer_value = request.headers.get('referer', '')
    data = referer_value if referer_value else 'default'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
