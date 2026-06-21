# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest32157(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = '%s' % str(forwarded_ip)
    request.session['data'] = str(data)
    return {"updated": True}
