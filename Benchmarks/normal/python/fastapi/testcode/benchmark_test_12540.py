# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest12540(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = forwarded_ip if forwarded_ip else 'default'
    request.session['user'] = str(data)
    return {"updated": True}
