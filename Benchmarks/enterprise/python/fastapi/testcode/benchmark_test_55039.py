# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest55039(request: Request):
    referer_value = request.headers.get('referer', '')
    with open('/var/app/data/' + str(referer_value), 'r') as fh:
        content = fh.read()
    return content
