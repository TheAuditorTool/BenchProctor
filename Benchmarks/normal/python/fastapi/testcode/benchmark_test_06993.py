# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest06993(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = '{}'.format(forwarded_ip)
    exec(str(data))
    return {"updated": True}
