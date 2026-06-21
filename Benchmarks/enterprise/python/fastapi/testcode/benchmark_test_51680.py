# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest51680(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = str(forwarded_ip).replace('\x00', '')
    request.session['user'] = str(data)
    return {"updated": True}
