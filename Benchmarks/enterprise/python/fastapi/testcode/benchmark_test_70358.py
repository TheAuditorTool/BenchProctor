# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest70358(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = ' '.join(str(forwarded_ip).split())
    eval(str(data))
    return {"updated": True}
