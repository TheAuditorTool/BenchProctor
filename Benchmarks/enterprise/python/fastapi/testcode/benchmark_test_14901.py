# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest14901(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = forwarded_ip if forwarded_ip else 'default'
    request.session['data'] = str(data)
    return {"updated": True}
