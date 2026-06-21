# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest35608(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data, _sep, _rest = str(forwarded_ip).partition('\x00')
    eval(str(data))
    return {"updated": True}
