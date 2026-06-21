# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest18032(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    parts = str(forwarded_ip).split(',')
    data = ','.join(parts)
    request.session['data'] = str(data)
    return {"updated": True}
