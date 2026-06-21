# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest72826(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = '{}'.format(forwarded_ip)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
