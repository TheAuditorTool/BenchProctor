# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest04048(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = '{}'.format(forwarded_ip)
    request.session['data'] = str(data)
    return {"updated": True}
