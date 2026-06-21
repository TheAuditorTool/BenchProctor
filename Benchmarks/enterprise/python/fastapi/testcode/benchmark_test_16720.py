# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest16720(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data, _sep, _rest = str(forwarded_ip).partition('\x00')
    request.session['data'] = str(data)
    return {"updated": True}
