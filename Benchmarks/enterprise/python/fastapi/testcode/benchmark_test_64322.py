# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest64322(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = '{}'.format(forwarded_ip)
    result = 100 / int(str(data))
    return {"updated": True}
