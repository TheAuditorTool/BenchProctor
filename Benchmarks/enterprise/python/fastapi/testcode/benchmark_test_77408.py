# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest77408(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    request.session['data'] = str(forwarded_ip)
    return {"updated": True}
