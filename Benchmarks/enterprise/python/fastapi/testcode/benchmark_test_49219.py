# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest49219(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = '%s' % str(forwarded_ip)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
