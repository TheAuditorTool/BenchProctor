# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest42872(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = '%s' % str(forwarded_ip)
    request.session['user'] = str(data)
    return {"updated": True}
