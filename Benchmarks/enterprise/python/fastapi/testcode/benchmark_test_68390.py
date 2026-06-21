# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest68390(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = str(forwarded_ip).replace('\x00', '')
    eval(str(data))
    return {"updated": True}
